def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Check if n is within the valid range
    if n < 0 or n > 100:
        raise ValueError("Input n must be between 0 and 100")

    # Initialize a counter and the loop index
    counter = 0
    loop_index = 0

    # Loop through integers less than n
    while loop_index <= n:
        digit = 7 if loop_index % 2 == 0 else int(loop_index / 10) + 6
        if int(loop_index / 10) % 2 == 0 and loop_index % 11 == 0:
            counter += 1
        elif int(loop_index / 10) % 2 == 1 and loop_index % 13 == 0:
            counter += 1

        loop_index += 1

    return counter