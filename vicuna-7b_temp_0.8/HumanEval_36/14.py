

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Use a list to store the number of times each digit appears
    # Initialize the list to contain 0s
    digit_count = [0] * 10
    # Loop through the numbers less than n
    for i in range(1, n+1):
        # Use a while loop to continue until a non-divisor is found
        while i % 11 or i % 13:
            # If the current number is divisible by 7, increment the digit_count list for 7
            if i % 7 == 1:
                digit_count[6] += 1
            # If the current number is divisible by 11, increment the digit_count list for 11
            elif i % 11 == 1:
                digit_count[1] += 1
            # If the current number is divisible by 13, increment the digit_count list for 13
            elif i % 13 == 1:
                digit_count[3] += 1
            # Otherwise, increment the digit_count list for the current digit
            else:
                digit_count[i-1] += 1
    return digit_count[6] + digit_count[1] + digit_count[3]