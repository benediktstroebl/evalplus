def tri(n):
    sequences, last = [1], 3
    for _ in range(n):
        if _ % 2 == 0:
            sequences.append(last / 2 + 1)
        else:
            sequences.append(sequences[-1] + sequences[-2] + last)
        last = sequences[-1]
    return sequences