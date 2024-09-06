

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize list to store the count of the number in the range 0 to 9
    count = [0] * 10
    # Loop through the numbers and check if it is divisible by 11, 13, and 3
    for i in range(n):
        if i % 11 == 0:
            # If the number is divisible by 11, check if it is divisible by 13
            if i % 13 == 0:
                # If it is divisible by 13, add 7 to the count of the number
                count[i // 13] += 1
            else:
                # If it is not divisible by 13, add 1 to the count of the number
                count[i // 13] += 1
        else:
            # If the number is not divisible by 11, check if it is divisible by 3
            if i % 3 == 0:
                # If it is divisible by 3, add 1 to the count of the number
                count[i // 3] += 1
            else:
                # If it is not divisible by 3, add 1 to the count of the number
                count[i // 3] += 1
    # Return the count of the number in the range 0 to 9
    return [count[i] for i in range(0, 10)]
