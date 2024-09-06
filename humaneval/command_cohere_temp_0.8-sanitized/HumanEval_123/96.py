def get_odd_collatz(n):
    odd_seq = [x for x in collatz_seq(n) if x % 2 == 1]
    odd_seq.sort()
    return odd_seq
def collatz_seq(n):
    if n == 1:
        return [1]
    else:
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq