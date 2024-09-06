def tri(n):
    result = [1, 3]
    if n > 1:
        result += [tri_even(n)]
        result += [tri_odd(n)]
    return result[:n+1]
def tri_even(n):
    return 1 + n // 2
def tri_odd(n):
    return tri_odd(n - 1) + tri_even(n - 2) + tri_even(n + 1)