def largest_smallest_integers(lst):
    if not positive_integers(lst) and not negative_integers(lst):
        return (None, None)
    elif len(lst) == 0:
        return (None, None)
    else:
        # Find the largest and smallest integers
        a, b = max(lst), min(lst)
        return (a, b)
def positive_integers(lst):
    return any(x > 0 for x in lst)
def negative_integers(lst):
    return all(x < 0 for x in lst)