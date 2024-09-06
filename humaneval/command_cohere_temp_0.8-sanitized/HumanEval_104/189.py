def unique_digits(ls):
    """Returns sorted list of elements in input list 'ls' 
    that have only digit values > 4."""
    return [x for x in ls if any(int(y) > 4 for y in str(x))]