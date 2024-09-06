def next_smallest(lst):
    if len(lst) < 2:
        return None
    mins = min(lst)
    sec_mins = mins + 1
    for n in lst:
        if n == secs_mins:
            return secs_mins
        if n > secs_mins and n < mins:
            mins = n
            secs_mins = n
    return secs_mins