```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(16))  # Output: 8
print(largest_divisor(20))  # Output: 10
```

However, a more optimized and Pythonic way to achieve this is by using a while loop or the math.gcd function.

Here's a revised version of the function:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(16))  # Output: 8
print(largest_divisor(20))  # Output: 10
```

Or even more concise:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(16))  # Output: 8
print(largest_divisor(20))  # Output: 10
```

You can calculate that by dividing n by each integer from n down to 1 until you find a divisor:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return max(i for i in range(n-1, 0, -1) if n % i == 0)


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(16))  # Output: 8
print(largest_divisor(20))  # Output: 10
```
However, if n is a prime number, the function will return 1 because 1 is the only number less than a prime number which is a divisor of it.