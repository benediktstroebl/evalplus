def largest_smallest_integers(lst):
    # If list is empty, return None for both values
    if not lst:
        return None, None

    # Search for negative and positive integers only
    nans = len(lst)
    lst = [num for num in lst if num >= 0]

    # Find the largest of negative integers
    largest_neg = max(lst) if nans == 1 else None

    # Find the smallest of positive integers
    smallest_pos = min(lst) if lst else None

    return largest_neg, smallest_pos