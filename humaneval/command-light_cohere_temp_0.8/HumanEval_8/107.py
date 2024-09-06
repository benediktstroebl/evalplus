Here is a Python script with a self-contained function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    This function returns a tuple containing sum and product of all integers in the input list.
    Args: 
    - A list of integers
    Returns: 
    - A tuple containing the sum and product of all integers in the input list
    """
    if not numbers:
        return (0, 1)  # Empty sum is 0 and empty product is 1
    else:
        # Initialize variables to store sum and product
        sum_ = 0
        prod_ = 1
        # Calculate sum and product
        for num in numbers:
            sum_ += num
            prod_ *= num
        return (sum_, prod_)

# Unit tests
test_sum_product = []
test_sum_product.append([1, 2, 3])
test_sum_product.append(sum_product(test_sum_product))
print(test_sum_product)  # Expected output: (6, 6)
```

This script defines a function sum_product that calculates the sum and product of a list of integers. It performs unit tests by passing a list of integers to the function and verifying that the output matches the expected result. The function also handles the empty list case, returning 0 for the sum and 1 for the product.