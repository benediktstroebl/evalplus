```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check each number if it's a divisor of n
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i
```

However, the above solution is not efficient as it checks every number from `n-1` down to `1`.

A more efficient solution is to only check up to the square root of `n`:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check each number if it's a divisor of n, up to the square root of n
    for i in range(n-1, int(math.sqrt(n)), -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i
    # If no divisor is found, return 1 (since 1 is a divisor of every number)
    return 1
```

But the most efficient way to solve this problem is to use the property that the largest divisor of `n` that is less than `n` is the same as the largest divisor of `n` that is greater than `n` divided by 2. This is because all numbers have a pair of divisors (i.e., a divisor and its corresponding quotient). Since we want to find the largest divisor that is less than `n`, if we divide `n` by 2, we will get a number that has the same or smaller divisors than `n`. We can then find the largest divisor of this new number, and it will be the same as the largest divisor of `n`. This way, we can avoid a loop and get the result in O(sqrt(n)) time complexity:

```python
import math

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Divide n by 2 and find the largest divisor of the new number
    largest = 1
    x = n
    while x > 1:
        x = math.floor(x / 2)
        largest = math.floor(n / x)
    return largest
```