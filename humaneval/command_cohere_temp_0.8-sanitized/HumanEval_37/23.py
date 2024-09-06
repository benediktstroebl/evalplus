def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)