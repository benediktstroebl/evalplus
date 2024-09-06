def get_odd_collatz(n):
    odd_seq = [y for y in collatz_sequence(n) if y % 2 == 1]
    odd_seq.sort()
    return odd_seq
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence