def tri(n):
    sequence, result = [], []
    sequence.append(3)
    result.append(3)
    if n == 1:
        return result
    for i in range(2, n + 1):
        if i % 2 == 1:
            sequence.append(sum(sequence[-3:]))
            result.append(sequence[-1])
        else:
            sequence.append(1 + i // 2)
            result.append(sequence[-1])
    return result