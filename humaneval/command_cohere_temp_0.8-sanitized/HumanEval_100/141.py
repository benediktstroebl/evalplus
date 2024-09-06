def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + [int(n % 2 == 0 and n + 2 or n + 1)] * (n - 2)