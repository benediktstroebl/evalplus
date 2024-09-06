def sort_even(l):
    even, odd = zip(*[iter(l)]*2)
    return list(odd)+list(sorted(even))