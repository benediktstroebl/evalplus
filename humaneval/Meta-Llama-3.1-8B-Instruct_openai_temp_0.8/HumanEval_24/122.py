```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    def is_divisor(d: int) -> bool:
        """ Check if a number d is a divisor of n.
        Args:
        d (int): The number to check.
        
        Returns:
        bool: True if d is a divisor of n, False otherwise.
        """
        return n % d == 0

    for i in range(n - 1, 0, -1):
        if is_divisor(i):
            return i
    return None
```
However, a more efficient solution would be to directly iterate down from n to 1 and check each number if it's a divisor, which is shown below:

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None
```
This script works by checking all numbers from n-1 down to 1. If a number is found that divides n evenly (i.e., n % i == 0), it is the largest divisor of n and is returned. If no such divisor is found, None is returned (though in the case of a prime number, this would indicate the number itself is the largest divisor which isn't less than itself).