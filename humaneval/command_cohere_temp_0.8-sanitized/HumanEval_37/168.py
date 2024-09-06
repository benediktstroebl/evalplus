def sort_even(l):
    even, odd = zip(*[(i, val) for i, val in enumerate(l) if i % 2 == 0])
    return [odd[i] for i in range(len(odd))] + [even[i] for i in sorted(range(len(even)))]