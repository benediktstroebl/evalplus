def exchange(lst1, lst2):
    res = "NO"
    even_idxs = [i for i, x in enumerate(lst1) if x % 2 == 0]
    if len(even_idxs) > 0:
        # try swapping
        try:
            lst1, lst2 = zip(lst1, lst2)
            lst1, lst2 = list(zip(*sorted(zip(lst1, lst2), key=lambda i_n_j: i_n_j[0] != i_n_j[1])))
            if all(x % 2 == 0 for x in lst1) and all(x % 2 != 0 for x in lst2):
                res = "YES"
        except Exception as e:
            pass
    return res