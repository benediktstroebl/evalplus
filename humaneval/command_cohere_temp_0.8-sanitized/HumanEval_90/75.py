def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    largest = sorted(lst)[-2]
    return largest if lst.index(largest) == len(lst) - 1 else None