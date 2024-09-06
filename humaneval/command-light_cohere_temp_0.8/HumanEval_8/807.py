Here's a self-contained Python function that calculates the sum and product of integers in a list:
```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result_sum = sum(numbers)
    result_product = 1
    for num in numbers:
        result_product *= num
    return (result_sum, result_product)
```

This function takes a list of integers as input and returns a tuple of two integers: the sum and the product of all the integers in the list. The sum is calculated using the `sum()` function and the product is calculated using a loop.

The function is then tested with different inputs to ensure it's working correctly.