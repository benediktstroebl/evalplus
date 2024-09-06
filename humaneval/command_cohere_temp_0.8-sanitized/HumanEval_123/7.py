def get_odd_collatz(n):
    odd_seq = [x for x in collatz_seq(n) if x % 2 != 0]
    return sorted(odd_seq)
def collatz_seq(n):
    if n == 1:
        return [1]
    else:
        odd_numbers = [n]
        while len(odd_numbers) > 0:
            for i in odd_numbers:
                if i % 2 == 0:
                    yield i // 2
                else:
                    yield i * 3 + 1
            odd_numbers = [x for x in odd_numbers if x % 2 != 0]