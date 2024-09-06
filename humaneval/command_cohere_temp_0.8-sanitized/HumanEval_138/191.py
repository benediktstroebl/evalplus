def is_equal_to_sum_even(n):
    # Check whether the given number can be expressed as the sum of four even positive numbers
    # By factoring the number into prime factors, and evaluating the sum of even factors, we arrive at the solution
    if n % 2 == 0: 
        even_factors = n // 2
        sum_even_factors = even_factors // 2
        return n == sum_even_factors * 4
    else:
        return False