def next_smallest(lst):
    def check_second_smallest(lst):
        lst.sort()
        if len(lst) < 2:
            return None
        else:
            return lst[1]

    if len(lst) < 1:
        return None
    if len(lst) == 1:
        return None if lst[0] == lst[0] else lst[0]
    return min(check_second_smallest(set(lst)), check_second_smallest(set(lst)[1:]))