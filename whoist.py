# 'domain_name':          r'Domain Name: *(.+)',
#         'registrar':            r'Registrar: *(.+)',
#         'whois_server':         r'Whois Server: *(.+)',
#         'referral_url':         r'Referral URL: *(.+)',  # http url of whois_server
#         'updated_date':         r'Updated Date: *(.+)',
#         'creation_date':        r'Creation Date: *(.+)',
#         'expiration_date':      r'Expir\w+ Date: *(.+)',
#         'name_servers':         r'Name Server: *(.+)',  # list of name servers
#         'status':               r'Status: *(.+)',  # list of statuses
#         'emails':               EMAIL_REGEX,  # list of email s
#         'dnssec':               r'dnssec: *([\S]+)',
#         'name':                 r'Registrant Name: *(.+)',
#         'org':                  r'Registrant\s*Organization: *(.+)',
#         'address':              r'Registrant Street: *(.+)',
#         'city':                 r'Registrant City: *(.+)',
#         'state':                r'Registrant State/Province: *(.+)',
#         'zipcode':              r'Registrant Postal Code: *(.+)',
#         'country':              r'Registrant Country: *(.+)',
#             registrador = 'PDR Ltd. d/b/a PublicDomainRegistry.com'
#             serverWhois = w.whois_server
#             expiracion = w.expiration_date
#             creacion = w.creation_date
#             dominio = w.name

import whois
import os


with open("dominios.txt", "r") as archivo:

    for linea in archivo.read().splitlines():
        try:
            w = whois.whois(linea)
            whoiSer = 'whois.publicdomainregistry.com'
            serverWhois = w.whois_server

            destFile = r"act.txt"
            if serverWhois == whoiSer:
                destFile = r"act.txt"
                with open(destFile, 'a') as f:
                    f.write(linea+"\n")
                # print('true' + " " + linea)
            else:
                destFile = r"noact.txt"
                with open(destFile, 'a') as f:
                    f.write(linea+"\n")
            # print (str(serverWhois + " " + linea))
        except:
            destFile = r"deleteDomain.txt"
            with open(destFile, 'a') as f:
                f.write(linea+"\n")
