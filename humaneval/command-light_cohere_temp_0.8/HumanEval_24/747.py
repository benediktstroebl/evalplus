```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n that divides it evenly.
    """
    The number is always even divisible by 2, so we only need to find the first such number.

    We start with 2, 3, and then the next odd numbers until the number doesn't divide the input number.

    Return the fact.

    1.
    """
    

    if the ith number is divisible by n
    """

    # check first odd number
    if n % 2 == 0:
        return 2
    # check second odd number
    if n % 4 == 1:
        return 3
    # check for other odd numbers
    for i in range(5, n + 2, 2):
        if n % i == 0:
            return i
    else:
        return n
```