

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            count += 1
        elif i % 3 == 0:
            print('Fizz')
            count += 1
        elif i % 5 == 0:
            print('Buzz')
            count += 1
    
