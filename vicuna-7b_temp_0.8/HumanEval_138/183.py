
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is even
    if n % 2 == 0:
        return False
    # Check if n is 2^k for some k
    if n == 2**k for k in range(4, 11):
        return False
    # Check if n is 2*2^k + 2*2^(k+1) for some k
    if n == 2*2**k + 2*2^(k+1) for k in range(4, 11):
        return False
    # Check if n is 2*2^k - 2*2^(k+1) for some k
    if n == 2*2**k - 2*2^(k+1) for k in range(4, 11):
        return False
    # If none of the above conditions are true, then n can be written as the sum of exactly 4 positive even numbers
    return True