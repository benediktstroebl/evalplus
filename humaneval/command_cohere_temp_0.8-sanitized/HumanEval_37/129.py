def sort_even(l):
    even = [x for x in l if isinstance(x, int) and x % 2 == 0]
    odd = [x for x in l if isinstance(x, int) and x % 2 != 0]
    return odd + sorted(even)