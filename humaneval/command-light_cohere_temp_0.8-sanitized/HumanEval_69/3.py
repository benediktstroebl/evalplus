def search(lst):
    """Return the greatest integer that occurs more than zero times in the list, or -1 if no such integer exists."""
    freq = 1 # Initialize frequency counter.
    for num in lst:
        freq += 1
    return max([num for num in lst if num > 0 and freq == num]) or -1