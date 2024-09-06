

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize the counters for number of 7s and number of fizzbuzzes
    sevens = 0
    fbzs = 0

    # Initialize number to be tested
    num_to_check = n - 1

    while num_to_check > 0:
        # If the current number is divisible by 7, increment the seven counter
        if num_to_check % 7 == 0:
            sevens += 1

        # If the current number is divisible by 11 but not by 13, increment the fizzbuzz counter
        elif num_to_check % 11 == 0 and num_to_check % 13 != 0:
            fbzs += 1

        # If the current number is divisible by 11 and by 13, increment both counters
        elif num_to_check % 11 == 0 and num_to_check % 13 == 0:
            fbzs += 1
            sevens += 1

        # Increment the "number to check" counter
        num_to_check -= 1

    # Return the quotient of the two counters
    return fbzs // sevens
