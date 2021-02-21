# Coded By : NumeX
# Team : RAS CYBER TEAM | IMSC | GHX OFFICIAL
# Community : Maupumd | IT-World

import requests # pip install requests

print("""
# Coded By : NumeX
# Team : RAS CYBER TEAM | IMSC | GHX OFFICIAL
# Community : Maupumd | IT-World
""")
target = input("\n[~] Enter Target : ")
lol = requests.get(f"https://api.hackertarget.com/nmap/?q={target}")
result = lol.text.strip(" ( https://nmap.org/ ) ")
print(f"\n{result}")
input("\nEnter Any Key For Close...")