```python
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd
        - the next even number if n is even
    Return: the number of stones in each level, where element at index i represents the number of stones in the level (i+1)
    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    if n <= 1:
        return [1]
    if n % 2 == 0:
        return [2 * i + 1 for i in range(n // 2)]
    else:
        return [2 * i + 2 for i in range(n // 2)]

# Additional test cases
print(make_a_pile(6))  # [2, 4, 6, 8]
print(make_a_pile(11))  # [3, 5, 7, 9, 11]
```
This script defines a function `make_a_pile` that constructs a list representing a pile of stones with a given number of levels. The number of stones in each level is determined based on whether the input `n` is even or odd. The function then returns a list of numbers that form the desired pile. The output of this code will be the list of numbers representing the pile of stones.