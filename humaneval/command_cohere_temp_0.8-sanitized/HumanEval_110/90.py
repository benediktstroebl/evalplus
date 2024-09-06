def exchange(lst1, lst2):
    res = 'NO'
    # check if any element of lst1 is odd
    if any(el % 2 for el in lst1):
        # check if any even element of lst2 is not in lst1
        if all(el % 2 == 0 for el in lst2) and all(el in lst1 for el in lst1 if el % 2 == 0):
            res = 'YES'
    return res