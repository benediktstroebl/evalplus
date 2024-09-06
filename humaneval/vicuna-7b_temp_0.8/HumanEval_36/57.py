

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # A stack to hold the running total of fizz and buzz.
    stack = []
    # The current number.
    current_number = 1
    # A set to hold the divisors of n.
    divisors = set()
    # A set to hold the numbers that divide only by 11 or 13.
    fizz_buzz_numbers = set()
    # Keep track of the number of times 7 appears in the stack.
    count_7 = 0
    
    while current_number <= n:
        # If current_number is divisible by 11, put it in the fizz_buzz_numbers set.
        if current_number % 11 == 0:
            fizz_buzz_numbers.add(current_number)
            count_7 += 1
            divisors.add(11)
            current_number += 11
        # If current_number is divisible by 13, put it in the fizz_buzz_numbers set.
        elif current_number % 13 == 0:
            fizz_buzz_numbers.add(current_number)
            count_7 += 1
            divisors.add(13)
            current_number += 13
        # If current_number is not divisible by 11 or 13, it goes on the stack.
        else:
            stack.append(current_number)
            current_number += 1
    
    # Return the number of times 7 appears in the stack.
    return count_7
