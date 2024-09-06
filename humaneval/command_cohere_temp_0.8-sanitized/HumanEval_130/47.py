def tri(n):
    Sequence = [1, 3]
    if n <= 1:
        return Sequence[:n+1]
    else:
        a, b, c = Sequence[-1:]
        odd = n % 2
        even = not odd
        x1 = a if odd else a + b
        x2 = b if even else b + c
        x3 = c if odd else c + a
        Sequence.extend([x1, x2, x3])
        return Sequence[:n+1]