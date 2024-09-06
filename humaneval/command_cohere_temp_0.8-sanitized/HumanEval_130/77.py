def tri(n):
    result = [1, 3]
    if n > 1:
        result.extend(
            tri(x) + tri(x - 1) + tri(x + 1) for x in range(2, n + 1, 2)
        )
    result.append(n)
    return result