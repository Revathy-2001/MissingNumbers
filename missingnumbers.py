
n = int(input())
lst = []
for i in range(n):
  v = int(input())
  lst.append(v);

lastNo = max(lst)
cnt = 0
lst1 = []
for i in range(lastNo):
  cnt+=1
  lst1.append(cnt)

if(lst == lst1):
  print('good job')
else:
  lst.sort();
  new = [x for x in lst1 if x not in lst]
  for i in new:
    print(i)