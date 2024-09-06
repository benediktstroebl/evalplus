def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(a, b):
    mi = max(a[1], b[1])
    ma = min(a[0], b[0])
    if ma > mi:
        return "NO"
    if is_prime(mi - ma + 1):
        return "YES"
    else:
        return "NO"