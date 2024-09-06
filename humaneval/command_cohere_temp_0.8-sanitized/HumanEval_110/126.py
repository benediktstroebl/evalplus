def exchange(lst1, lst2):
    res = 'NO'
    # Check if any element of lst1 is odd
    if any(x % 2 for x in lst1):
        # Exchange odd elements with lst2
        lst1, lst2 = lst2, lst1
        res = 'YES'
    return res