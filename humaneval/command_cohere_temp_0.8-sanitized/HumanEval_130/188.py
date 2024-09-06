def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    sequence = [1, 3]
    if n % 2 == 0:
        for i in range(1, n):
            x = 1 + i / 2
            sequence.append(x)
    else:
        for i in range(2, n + 1):
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i])
    return sequence