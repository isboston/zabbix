from pyzabbix import ZabbixAPI
import csv


zapi = ZabbixAPI('your zabbix server')
zapi.login(api_token='your token')
print("Connected to Zabbix API Version %s" % zapi.api_version())


filehosts = 'test.csv'
f = csv.reader(open(filehosts), delimiter=';')
next(f)


def hostCreate(hostname, visible, ip, departament, room):
    hostcriado = zapi.host.create(
            host = hostname,
            name = visible,
            status = 0,
            groups = [{
                "groupid": 25
            }],
            interfaces = [{
                "type": 2,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": 161,
                "details": {
                     "version": 3,
                     "bulk": 0,
                     "securityname": "Zabbix",
                     "contextname": "",
                     "securitylevel": 2,
                     "authprotocol": 0,
                     "privprotocol": 0,
                     "authpassphrase": 'your password',
                     "privpassphrase": 'your password'}
            }],
            tags = [{
              "tag": "кабинет",
              "value": room
            },
            {
              "tag": departament,
              "value": ""
            }],

            templates = [{
                "templateid": 10223
            }]
        )

for [hostname, visible, ip, departament, room] in f:
        hostCreate(hostname, visible, ip, departament, room)
        print("Create %s"%hostname)
exit()
