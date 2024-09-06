def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + [(n+1) if n % 2 else n + 2] * (n - 1)