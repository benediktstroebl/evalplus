

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for special case of n == 0
    if n == 0:
        return 0
    
    # Initialize a list to store the number of times each digit appears
    num_digits = [0] * 10
    
    # Loop through the numbers from 1 to n
    for i in range(1, n+1):
        # Check if n is divisible by 11
        if n % 11 == 0:
            # Check if the current digit is 7
            if i % 13 == 0:
                # If it is, increment the count for the digit 7
                num_digits[7] += 1
            # If it is not, increment the count for the digit 13
                num_digits[13] += 1
        # Check if n is divisible by 13
        elif n % 13 == 0:
            # Check if the current digit is 7
            if i % 13 == 0:
                # If it is, increment the count for the digit 7
                num_digits[7] += 1
            # If it is not, increment the count for the digit 13
                num_digits[13] += 1
        else:
            # Otherwise, increment the count for the current digit
            num_digits[i-1] += 1
    
    # Return the number of times each digit appears
    return [num_digits[digit] for digit in range(1, 10)]
