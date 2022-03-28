import jieba
f = open("f:/白话二十四史之【隋书】.txt", "r" , encoding = "utf-8" ) # 打开指定文件，创建1个文件
txt = f.read()

words = jieba . lcut(txt)
print(words)
counts = {}
for word in words:
    if len(word) ==1:
        continue
    else:
        counts[word] = counts.get(word , 0) + 1
print(counts)
items = list(counts.items())
items.sort( key = lambda x:x[1], reverse = True)
print(items)
for i in range(20):
    print(items[i][0], items[i][1])