def exchange(lst1, lst2):
    res = 'NO'
    # Check if any element of lst1 is odd
    if any(val % 2 for val in lst1):
        # Exchange odd elements with elements from lst2
        lst1[:], lst2[:] = lst2, lst1
        res = 'YES'
    return res