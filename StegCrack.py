#!/usr/bin/python


import base64


base = """IyEvdXNyL2Jpbi9weXRob24KCmltcG9ydCBvcywgc3lzCgpmaWxlID0gc3lzLmFyZ3ZbMV0KbGlz
dCA9IHN5cy5hcmd2WzJdCgpvcy5zeXN0ZW0oJ2NvbW1hbmQgLXYgc3RnZWhpZGUgPi9kZXYvbnVs
bCAyPiYxIHx8IGFwdC1nZXQgaW5zdGFsbCBzdGVnaGlkZSAteSA+L2Rldi9udWxsJykKcHJpbnQg
KGYiXG5cMDMzWzkxbSBDcmFja2luZyB7ZmlsZX0uLi4uLiIpCgp0cnk6CiAgICBvcy5zeXN0ZW0o
ZicnJyBcbiBmb3IgaSBpbiAkKGNhdCB7bGlzdH0pOyBkbyBzdGVnaGlkZSAtLWV4dHJhY3QgLXNm
IHtmaWxlfSAtcCAkaSAyPi9kZXYvbnVsbCAmJiBlY2hvIC1lICIgXDAzM1s5Mm0gUGFzc3dvcmQ6
ICRpIiAmJiBicmVhazsgZG9uZScnJykKZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0IGFzIGs6CiAg
IHByaW50ICgnXDAzM1s5Nm0gU3RvcHBlZCEnKQogICBzeXMuZXhpdCgpCgo="""

print (base)

#try:
 #   exec (base64.b64decode(base))
#except IndexError as i:
 #   print ('\033[91m Syntax: python StegCrack.py <File> <Wordlist_to_Crack>')
