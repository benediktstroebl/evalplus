def tri(n):
    res = [1, 3]
    if n > 1:
        res += [tri_even(n) for _ in range(n - 2)]
        res += [tri_odd(n)]
    return res[:n + 1]
def tri_even(n):
    return 1 + n // 2
def tri_odd(n):
    return tri_odd(n - 1) + tri_even(n) + tri_odd(n + 1)