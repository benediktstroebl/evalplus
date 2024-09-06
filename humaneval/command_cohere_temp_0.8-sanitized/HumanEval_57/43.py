def monotonic(lst):
    if len(lst) < 2:
        return True
    a = lst[0]
    b = lst[1]
    # checking for increasing sequence
    if a <= b:
        for i in range(2, len(lst)):
            if lst[i] <= lst[i - 1]:
                continue
            else:
                return False
    # checking for decreasing sequence
    else:
        for i in range(2, len(lst)):
            if lst[i] >= lst[i - 1]:
                continue
            else:
                return False
    return True