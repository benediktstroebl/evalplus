def sort_third(l):
    l3 = [e for e in l if e%3==0]
    l3.sort()
    return l[:len(l)//3*3]+l3+l[len(l)//3*3:]