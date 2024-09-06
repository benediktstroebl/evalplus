def sort_even(l):
    even = [e for e in l if e % 2 == 0]
    odd = [e for e in l if e % 2 != 0]
    return odd + sorted(even)