import re

regex = r".*((23\/Mar\/2009:(03:(28:(1[7-9])|([2-5][0-9]))|(09:[0-5][0-9]:[0-5][0-9])|(([3-5][0-9]):([0-5][0-9]):([0-5][0-9])))|(24\/Mar\/2009:(([0-1][0-9])|([2][0-3])):[0-5][0-9]:[0-5][0-9])|(25\/Mar\/2009:(([0][0-8]:[0-5][0-9]:[0-5][0-9])|(09:[0-4][0-9]:[0-5][0-9])|(09:5[0-1]:[0-5][0-9])|(09:52:([0-4][0-9])|(50)))).*OPTIONS.*HTTP\/.*401\s))"
log_file = r"C:/Users/ostap/Desktop/access.log.txt"


count = 0
match_list = []
with open(log_file, "r") as file:
    for line in file:
        for match in re.finditer(regex, line):
            match_text = match.group()
            match_list.append(match_text)
            print(match_text)
            count += 1
print(count)