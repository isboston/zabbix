from pyzabbix import ZabbixAPI
import csv


zapi = ZabbixAPI('your zabbix server')
zapi.login(api_token='your token')
print("Connected to Zabbix API Version %s" % zapi.api_version())


filehosts = 'test.csv'
f = csv.reader(open(filehosts), delimiter=';')
next(f)


def hostCreate(hostname, visible, ip):
    hostcriado = zapi.host.create(
            host = hostname,
            name = visible,
            status = 0,
            groups = [{
                "groupid": 6
            }],
            interfaces = [{
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": visible,
                "port": 10050
            }],
            tags = [{
                "tag": "proxmox",
                "value": ""
            }],
            templates = [{
                "templateid": 10001
            }]
        )

for [hostname, visible, ip] in f:
        hostCreate(hostname, visible, ip)
        print("Create %s"%hostname)
exit()
