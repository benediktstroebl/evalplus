def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + list(make_a_pile(len(str(n + 2)) % 2 + 1))