def next_smallest(lst):
    if len(lst) < 2:
        return None
    elif lst[-2] > lst[-1]:
        return lst[-2]
    else:
        return None