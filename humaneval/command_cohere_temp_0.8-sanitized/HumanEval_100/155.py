def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + [int((n % 2) + 1) if n % 2 else n + 2 for n in range(1, n)]