

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for divisibility by 11 and 13
    is_divisible_by_11 = n % 11 == 0
    is_divisible_by_13 = n % 13 == 0
    
    # Check if n is divisible by 7
    is_divisible_by_7 = n % 7 == 0
    
    # Check if n is 0 or not divisible by 7, 11, or 13
    if is_divisible_by_7 or not is_divisible_by_11 and not is_divisible_by_13:
        return 0
    
    # Check if n is divisible by 7 and write down its digits
    digits = str(n)
    for i, digit in enumerate(digits):
        if digit == 7:
            return i+1
    
    # If none of the above conditions are met, return 0
    return 0
