def tri(n):
    Sequence = [1, 3]
    if n <= 1:
        return Sequence[:n+1]
    else:
        j = 1
        sequence = Sequence[j:]
        for i in range(2, n + 1):
            if i % 2 == 0:
                sequence.append(1 + i // 2)
            else:
                x = tri(i - 1) + tri(i - 2) + tri(i + 1)
                sequence.append(x)
        return sequence[:n+1]