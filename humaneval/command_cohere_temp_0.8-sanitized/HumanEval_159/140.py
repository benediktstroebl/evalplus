def eat(n, need, rem):
    cout = []
    temp = n + need
    if temp > rem:
        temp = rem
    cout.append(n + temp)
    cout.append(rem - temp)
    return cout