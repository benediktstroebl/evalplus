def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + odd_even(n + 1)
def odd_even(num):
    odd_sequence = [x for x in range(1, num, 2)]
    even_sequence = [x for x in range(2, num, 2)]
    return odd_sequence if num % 2 else even_sequence