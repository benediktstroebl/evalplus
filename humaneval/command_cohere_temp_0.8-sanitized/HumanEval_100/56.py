def make_a_pile(n):
    if n == 0:
        return []
    return [n] + make_a_pile(n - 2) if n % 2 == 0 else [n] + make_a_pile(n - 1)