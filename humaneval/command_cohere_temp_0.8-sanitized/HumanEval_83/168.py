def starts_one_ends(n):
    return sum(int(x) >= 1 for x in iter(f'{1}{n}1'))