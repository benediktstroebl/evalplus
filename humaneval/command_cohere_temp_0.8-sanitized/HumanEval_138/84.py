def is_equal_to_sum_even(n):
    # Check whether the given number can be expressed as the sum of four even positive numbers
    # By factoring the number into prime factors, and evaluating whether it is possible to construct such sum
    if n < 0:
        return False
    while n % 2 == 0:
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n //= i
            if n == 0:
                return False
    return n == 1