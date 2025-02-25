from collections import deque
##print("First a Queue...")
q = deque();
data = ["tom", "jerry", "sylvestor"]
##
##for e in data:
##    q.append(e)
##    #print(q)
##print(q)
##
##item = q.popleft()
##print("Removed", item)
##print(q)
##
##
##q.append("goofy")
##q.append("pluto")
##
##print(q)
##
##while(len(q)>0):
##    print(q.popleft())
 #################################################STACK##########################################
print("Now a stack...")
s = q

for e in data:
    s.append(e)

print(s)

item = s.pop()
print("Popped", item)
print(s)

s.append("goofy")
s.append("pluto")

print(s)

while(len(s)>0):
    print(s.pop())

print(s)

