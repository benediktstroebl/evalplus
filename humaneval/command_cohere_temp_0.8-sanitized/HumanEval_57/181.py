def monotonic(lst):
    if len(lst) < 2:
        return True
    a = lst[0]
    b = lst[1]
    # check if the list is sorted in increasing order
    if a < b:
        for i in range(2, len(lst)):
            if lst[i] <= lst[i - 1]:
                continue
            else:
                return False
    # check if the list is sorted in decreasing order
    elif a > b:
        for i in range(2, len(lst)):
            if lst[i] >= lst[i - 1]:
                continue
            else:
                return False
    else:  # if two elements are equal, the list is not monotonic
        return False
    return True