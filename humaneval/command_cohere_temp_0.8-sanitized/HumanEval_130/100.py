def tri(n):
    result = [1, 3]
    if n >= 2:
        result.extend(f(n) for f in (lambda n: 1 + n//2 if n % 2 == 0 else
                                      lambda n: tri(n - 1) + tri(n - 2) + tri(n + 1))
                                     for _ in range(n - 2))
    return result