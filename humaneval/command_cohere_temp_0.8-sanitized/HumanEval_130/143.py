def tri(n):
    sequence, last_odd, last_even = [], 1, 3
    while len(sequence) < n + 1:
        if len(sequence) % 2 == 0:
            sequence.append(last_even)
            last_even = last_even + last_odd + next_odd
            last_odd = next_odd
        else:
            sequence.append(last_odd)
            last_odd = last_odd + last_even + next_even
            last_even = next_even
        next_odd = 1 + (len(sequence) - 1) // 2
        next_even = sequence[len(sequence) - 2]
    return sequence