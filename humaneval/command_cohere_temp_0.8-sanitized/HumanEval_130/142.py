def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    trib = [0, 0, 0]
    for i in range(2, n + 1):
        if i % 2 == 0:
            trib.append(1 + i // 2)
        else:
            trib.append(trib[i - 1] + trib[i - 2] + trib[i + 1])
    return trib