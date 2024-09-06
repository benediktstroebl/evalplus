def tri(n):
    seq, last_odd, last_even = [], 1, 3
    while len(seq) < n + 1:
        if len(seq) % 2 == 0:
            seq.append(last_even)
            last_even = last_even + last_odd + seq[-1]
        else:
            seq.append(seq[-1] + seq[-2] + last_odd)
            last_odd = seq[-1] + seq[-2] + last_even
    return seq[:n+1]