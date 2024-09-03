def make_a_pile(n):
    if n < 1:
        return []

    odd_stones = n // 2
    even_stones = n % 2

    return [i+1 for i in range(odd_stones+even_stones)]