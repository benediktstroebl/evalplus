def sort_even(l):
    even, odd = zip(*[(i, val) for i, val in enumerate(l) if i % 2 == 0])
    return [val for i, val in enumerate(l) if i % 2 == 1] + [sorted(even)]