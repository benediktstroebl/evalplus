

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # for i in range(n):
    #     if i % 11 == 0 or i % 13 == 0:
    #         print("FizzBuzz")
    #     elif i % 11 == 0:
    #         print("Fizz")
    #     elif i % 13 == 0:
    #         print("Buzz")
    #     else:
    #         print(i)
    count = 0
    for i in str(n):
        if i == "7":
            count += 1
        if i == "11":
            count += 1
        if i == "13":
            count += 1
    return count
