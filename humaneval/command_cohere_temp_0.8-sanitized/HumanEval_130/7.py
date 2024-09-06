def tri(n):
    Sequence = [1, 3]
    if n >= 1:
        Sequence.extend(Sequence[-2:] + [Sequence[-1] + Sequence[-2] + x for x in Sequence[1:-2]] + [Sequence[-1]])
    return Sequence[:n+1]