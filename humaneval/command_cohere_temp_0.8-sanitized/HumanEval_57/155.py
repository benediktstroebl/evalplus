def monotonic(lst):
    if len(lst) < 2:
        return True
    a = lst[0]
    b = lst[1]
    # if a==b, it's trivially true
    if a == b:
        return True
    # check if lst is sorted in ascending order
    if a < b:
        for i in range(2, len(lst)):
            if lst[i] <= lst[i - 1]:
                continue
            else:
                return False
    # check if lst is sorted in descending order
    elif a > b:
        for i in range(2, len(lst)):
            if lst[i] >= lst[i - 1]:
                continue
            else:
                return False
    else:
        return False