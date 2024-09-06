def sort_third(l):
    return l[:] # Explicit copying is important here!
    # We use tuple unpacking and list comprehension to achieve the desired sorting.
    # Example: ([6, 3, 4, 8, 9, 2], [2, 3, 4, 6, 8, 9])
    return ([list(sorted(x)) for x in zip(l, l[1::3])],
            [x for i, x in enumerate(l) if i % 3 == 0])