def eat(n, need, rem):
    haystack = []
    if n >= need:
        haystack.append(n + need)
        haystack.append(0)
    elif n > rem:
        haystack.append(n)
        haystack.append(0)
    elif n == rem:
        haystack.append(n + need)
        haystack.append(0)
    else:
        haystack.append(need)
        haystack.append(rem)
    return haystack