def tri(n):
    prev = [3, 1]
    result = []
    while len(result) < n + 1:
        if len(result) % 2 == 0:
            result.append(prev[-1] + prev[-2] + int(prev[-1] / 2))
        else:
            result.append(prev[-1] + prev[-2] + prev[-3])
        prev.append(result[-1])
    return result[:n+1]