def exchange(lst1, lst2):
    res = 'NO'
    # Check if any element of lst1 is odd
    if any(ele % 2 for ele in lst1):
        # Check if any odd element of lst1 is in lst2
        if any(ele % 2 for ele in lst2) and all(ele % 2 == 0 for ele in lst1):
            res = 'YES'
    return res