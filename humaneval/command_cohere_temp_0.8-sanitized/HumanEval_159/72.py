def eat(n, need, rem):
    eater = []
    if n + need > rem:
        eater.append(n + need)
        eater.append(0)
    elif n + need <= rem:
        eater.append(n + need)
        eater.append(rem - (n + need))
    return eater