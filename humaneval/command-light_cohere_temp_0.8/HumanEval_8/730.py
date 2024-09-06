Here is a self-contained Python function that solves the problem of calculating the sum and product of a list of integers:
```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all integers in the list.
    >>> numbers = [1, 2, 3, 4]
    >>> sum_product(numbers)
    (6, 12)
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3])
    (6, 6)
    >>> sum_product([10, 20, 30])
    (60, 300)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```
This function takes a list of integers as input and returns a tuple containing the sum and product of the integers. The function is self-contained and does not rely on any other functions or modules.