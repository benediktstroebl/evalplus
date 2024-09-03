def tri(n):
    result = [0, 1, 3]
    while len(result) < n + 1:
        if len(result) % 2 == 0:
            result.append(1 + result[-1] / 2)
        else:
            x = result[-1]
            y = result[-2]
            z = result[-3]
            result.append(x + y + z)
    return result[:n+1]