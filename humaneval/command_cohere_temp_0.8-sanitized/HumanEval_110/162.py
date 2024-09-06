def exchange(lst1, lst2):
    odd = lst1.pop()
    even = lst2.pop(0)
    if not lst1 or not lst2:
        return "NO"
    while lst1 and lst2:
        if lst1 and lst2:
            tmp = lst1.pop()
            lst2.append(tmp)
            tmp = lst2.pop(0)
            lst1.append(tmp)
        else:
            break
    if all(isinstance(n, int) and n % 2 == 0 for n in lst1):
        return "YES"
    return "NO"