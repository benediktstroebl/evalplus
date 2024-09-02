

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # count = 0
    # for num in range(1, n):
    #     if num % 11 == 0 or num % 13 == 0:
    #         count += number_of_sevens(num)
    # return count

    # Another way to do it...

    # return sum(number_of_sevens(n) for n in range(1, n) if n % 11 == 0 or n % 13 == 0)

    # Another way to do it...

    return sum(number_of_sevens(n) for n in range(1, n) if (n % 11 == 0 or n % 13 == 0))

