

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Use a list to store the possible FizzBuzz combinations
    fizz = [True, True, False]
    buzz = [True, False, True]
    combinations = [(fizz[i][j], buzz[i][j]) for i in range(len(fizz)) for j in range(len(buzz))]
    # For each number from 1 to n, check if it is divisible by 11 and 13
    # If it is, increment the appropriate FizzBuzz combination
    for i in range(1, n+1):
        for combination in combinations:
            if i % 11 == 0:
                combination[0] += 1
                combination[1] += 1
            if i % 13 == 0:
                combination[0] += 1
            if combination[0] > 0 and combination[1] > 0:
                yield i
