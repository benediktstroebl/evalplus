def tri(n):
    result = [0,1,3]
    if n >= 1:
        result += [tri_rec(n)]
    return result + [0]
def tri_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 1:
        return tri_rec(n - 1) + tri_rec(n - 2) + tri_rec(n + 1)
    else:
        return 1 + n / 2