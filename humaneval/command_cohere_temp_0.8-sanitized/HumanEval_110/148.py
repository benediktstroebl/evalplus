def exchange(lst1, lst2):
    res = 'NO'
    even_idxs = [i for i, x in enumerate(lst1) if x % 2 == 0]
    if len(even_idxs) > 0:
        # try swapping elements from lst2 into lst1 at even indices
        for idx in even_idxs:
            if lst1[idx] == lst2[idx]:
                continue
            # check if we can make lst1 all even via exchanges
            if lst1[idx] % 2 == 0:
                lst1[idx], lst2[idx] = lst2[idx], lst1[idx]
                res = 'YES'
                break
            else:
                lst1[idx], lst2[idx] = lst2[idx], lst1[idx]
        if res == 'YES':
            return res
        # reverse the swaps to restore the original order
        for idx in even_idxs:
            lst1[idx], lst2[idx] = lst2[idx], lst1[idx]
    return res