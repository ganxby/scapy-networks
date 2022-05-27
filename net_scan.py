import scapy
import scapy.all as scapy



def scan(ip):
    # scapy.arping(ip)
    # scapy.ls(scapy.Ether())

    apr_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') 
    arp_request_broadcast = broadcast/apr_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=3, verbose=False)[0]

    print("IP\t\t\tMAC Address\n")
    print("-----------------------------------------")


    client_list = []
    for element in answered_list:
        client_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        client_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

    #print('\n')
    #print(client_list)
    #print(answered_list.summary())


x = input(str('>> '))
scan(x)
