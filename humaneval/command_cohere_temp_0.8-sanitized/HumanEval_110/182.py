def exchange(lst1, lst2):
    even_found, odd_found = False, False
    for x in lst1:
        if x % 2:
            if even_found:
                return "NO"
            odd_found = True
        else:
            even_found = True
    return "YES"