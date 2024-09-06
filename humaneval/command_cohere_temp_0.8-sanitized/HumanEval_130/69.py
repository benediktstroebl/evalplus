def tri(n):
    seq, last_odd, last_even = [], 1, 3
    for i in range(n + 1):
        if i % 2 == 0:
            seq.append(last_even)
            last_even = last_even + 1
        else:
            seq.append(last_odd)
            last_odd = last_odd + last_even + seq[i - 2]
    return seq