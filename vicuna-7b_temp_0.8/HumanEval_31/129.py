

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n > 3 and n % 4 == 0:
        return False
    else:
        for i in range(5, int(n**0.5) + 1, 6):
            if n % i == 0:
                return False
        return True

def fibonacci(n):
    """Return the nth Fibonacci number using the recurrence relation.
    >>> fibonacci(10)
    55
    >>> fibonacci(20)
    841
    """
    a, b = 0, 1
    for i in range(n):
        if i == 0 or i == 1:
            yield a
        else:
            a, b = b, a + b

def factorial(n):
    """Return the factorial of a given number.
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    """
    if n == 0:
        return 1
    else:
        return n \* factorial(n-1)

def sum(numbers):
    """Return the sum of a list of numbers.
    >>> sum([1, 2, 3, 4])
    10
    >>> sum([0, -2])
    -2
    """
    return sum([a for a in numbers if a != 0])
