import sys
import string

# read file and words
word_cnt_dict = {}
total = 0
lines = sys.stdin.readline()
while lines !="":
    value_word = lines.split()
    key_word = value_word[0]
    cnt = int(value_word[1])
    total += cnt
    word_cnt_dict[key_word] = cnt
    lines = sys.stdin.readline()

# produce a histogram
for label,cnt in word_cnt_dict.items():
    print(label.ljust(15),"\t[",sep='',end='')
    per = int(cnt)*100//total
    for i in range(0,per,5):
        print("*",sep='',end='')
    print("] ", per,"%",sep='')