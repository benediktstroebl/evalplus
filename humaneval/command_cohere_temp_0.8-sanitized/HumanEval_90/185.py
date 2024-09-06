def next_smallest(lst):
    if len(lst) < 2:
        return None
    mins = min(lst)
    sec_mins = mins + 1
    for num in lst:
        if num == sec_mins:
            return num
        elif num > sec_mins:
            sec_mins = num
    return None