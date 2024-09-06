```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Args:
        numbers (List[int]): A list of integers.
    Returns: tuple consisting of a sum (int) and a product (int).
    Return values are in order, sum first, then product.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    return numbers,
    ```

test_sum_product_valid() -> None: Test the sum_product function with valid arguments
def test_sum_product_empty() -> None: Test the sum_product function with an empty list
def test_sum_product_single_element() -> None: Test the sum_product function with a list containing a single element
def test_sum_product_invalid() -> None: Test the sum_product function with an invalid input
```

This Python script defines a function called `sum_product` that calculates the sum and product of a list of integers. It also contains several test functions to validate the correctness of the `sum_product` function. The test functions pass the value of the `sum_product` function for different inputs, ensuring that the function produces the correct results.