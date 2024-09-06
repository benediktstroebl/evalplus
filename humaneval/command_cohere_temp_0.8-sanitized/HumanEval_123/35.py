def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 1:
            odd_collatz.append(sequence[-1])
        if sequence[-1] <= 4:
            break
        if sequence[-1] <= 2:
            sequence.pop()
            sequence.append(1)
        else:
            sequence.pop()
            sequence.append(sequence[-1] // 2)
    odd_collatz.sort()
    return odd_collatz