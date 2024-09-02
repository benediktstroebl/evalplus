

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Create a dictionary to store the number of times each digit appears
    # Add 11 and 13 separately so we can use them in the loop
    digits = {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 2, "8": 1, "9": 1}
    for i in range(1, n+1):
        # Check if the number is divisible by 11
        if i % 11 == 0:
            # If it is, increment the digit 7's count
            digits["7"] += 1
        # Check if the number is divisible by 13
        if i % 13 == 0:
            # If it is, increment the digit 7's count and the digit 13's count
            digits["7"] += 1
            digits["13"] += 1
        # If the number is not divisible by 11 or 13, increment the digit 7's count
        elif i % 11 != 0 and i % 13 != 0:
            digits["7"] += 1
    return [d for d in digits if d != 0]
