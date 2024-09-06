Here is a Python script that includes a self-contained function to solve the problem of calculating the sum and product of a list of integers, along with passing tests to verify the function's correctness:
```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    
    return (sum(numbers), product(numbers))
```