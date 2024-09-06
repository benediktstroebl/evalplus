def sort_third(l: list):
    l_split = [list(x) for x in zip(*[iter(l)] * 3)]
    return [x[i] for i, x in enumerate(l_split) if i % 3 == 0 and x != sorted(x)]