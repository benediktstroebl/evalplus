def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    """
    if not string or not substring:
        return 0

    count = 0
    idx = 0
    while idx < len(string):
        idx += 1
        nxt_idx = string.find(substring, idx)
        if nxt_idx == -1:
            break
        count += 1
        idx = nxt_idx
    return count