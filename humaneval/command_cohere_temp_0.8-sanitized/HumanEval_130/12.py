def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    result = [1, 3]
    if n % 2 == 0:
        for i in range(1, n):
            result.append(1 + i // 2)
    else:
        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2] + result[i])
    return result