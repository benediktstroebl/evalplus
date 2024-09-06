def tri(n):
    seq, last_odd, last_even = [], 1, 3
    while len(seq) < n + 1:
        if len(seq) % 2 == 0:
            seq.append(last_even)
            last_even = 1 + last_even / 2
        else:
            seq.append(sum([last_odd, last_even, last_odd + last_even]))
            last_odd, last_even = last_even, last_odd + last_even
    return seq[:n+1]