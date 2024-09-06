def tri(n):
    result = [0, 1, 3]
    while len(result) < n + 1:
        num = 1 if result[-1] % 2 == 0 else 0
        result.append(result[-1] + result[-2] + result[-3] + num)
    return result[:n+1]