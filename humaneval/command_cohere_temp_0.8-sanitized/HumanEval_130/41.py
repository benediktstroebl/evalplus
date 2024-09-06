def tri(n):
    sequence, last_odd, last_even = [], 1, 3
    while len(sequence) < n + 1:
        if len(sequence) % 2 == 0:
            sequence.append(last_even)
            last_even = last_even + last_odd + sequence[-1]
        else:
            sequence.append(last_odd)
            last_odd = last_odd + last_even + sequence[-1]
    return sequence