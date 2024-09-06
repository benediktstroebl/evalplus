def tri(n):
    sequence, result = [], []
    sequence.append(3)
    result.append(3)
    if n <= 1:
        return result[:n+1]
    for i in range(2, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
            result.append(sequence[-1])
        else:
            x, y = sequence[-1], sequence[-2]
            sequence.append(x + y + sequence[-(i + 1)])
            result.append(sequence[-1])
    return result