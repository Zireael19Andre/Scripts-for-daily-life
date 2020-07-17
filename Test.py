fh = open('/Users/zireael19andre/Desktop/input.txt')
match = {}
output=[]
for line in fh:
    line=line.rstrip()
    if ':' in line:
        key = line.split(':',1)[0]
        value = line.split(':',1)[1]
        match[key] = value
    else:
        m = line

for k,v in match.items():
    if int(m) % int(k) == 0:
        output.append(v)
        answer = ''.join([str(i) for i in output])
    else:
        if len(output) == 0:
            answer = m
print(answer)