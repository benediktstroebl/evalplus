def exchange(lst1, lst2):
    res = "NO"
    # check if any element of lst1 is odd
    if any(ele % 2 for ele in lst1):
        # check if any even element of lst2 is not in lst1
        if all(ele not in lst1 for ele in lst2 if ele % 2 == 0):
            res = "YES"
    return res