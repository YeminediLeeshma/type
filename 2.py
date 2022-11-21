s1=input()
s2=input()
s3=s2[1:]
cnt=0
for i in range(len(s1)):
    if s1[i]==s3:
        cnt=cnt+1
    else:
        pass
print(cnt)
