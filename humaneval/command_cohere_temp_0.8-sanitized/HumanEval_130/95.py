def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    trib = [1, 3]
    if n % 2 == 1:
        trib.extend(tri(n - 1) + tri(n - 2) + tri(n + 1))
    else:
        trib.extend([1 + n // 2] * (n // 2 + 1))
    return trib