def sort_even(l):
    even, odd = zip(*[iter(l)]*2)
    return [next(o) if i%2 else next(e) for i, (e, o) in enumerate(zip(even, odd))]