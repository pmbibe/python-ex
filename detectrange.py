def detect_ranges(l):
    list = []
    l.sort()
    print(l)
    i=0
    while i < len(l):
        if (l[i] + 1 not in l) and (i < len(l) - 1):
            print(l[i], end=',')
#            list.append(l[i])
            i +=1

        elif (l[i] + 1 not in l) and (i == len(l) - 1):
            print(l[i], end='')
            i +=1
        else:
            a = l[i]
            b = i
            while b < len(l)-1:
                if a+1 == l[b+1]:
                    a=l[b+1]
                    b+=1

                else:
                    break
            if (b == len(l) - 1):
                print("(%i,%i)" %(l[i], l[b]+1) , end='')
            else:
                print("(%i,%i)" % (l[i], l[b] + 1), end=',')
#            list.append("(%i,%i)" %(l[i], l[b]+1))
            i=b+1
    return list

a = detect_ranges([2,5,4,8,12,6,7,10,13,19,20,21,56,456,45,34,235,234,123,57,678])

#Solution

