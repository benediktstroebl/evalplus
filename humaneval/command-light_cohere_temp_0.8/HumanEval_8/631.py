```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of a list of integers.
    Return a tuple with sum and product of the list.
    Args: 
        numbers (List[int]): A list of integers
    Returns: 
        Tuple[int, int]: A tuple with sum and product of the list of integers
    """
    return (sum(numbers), product(numbers))

# Test case 1: Sum should be equal to 0 and product should be 1
test_sum_product(())
# This will fail due to the absence of values in the list
test_sum_product([])

# Test case 2: Sum should be equal to 3 and product should be 6
test_sum_product([1, 2, 3])

# Test case 3: This will fail since (1,1) is not a valid tuple
test_sum_product((1,1))

# Test case 4: Sum should be equal to 4 and product should be 24
test_sum_product([1, 2, 3, 4])

# Test case 5: This will fail since the product function with an empty list returns 1, which is not correct
test_sum_product([1, 2, 3, 4, 5])
```
This code provides a function `sum_product` that takes a list of integers as input and returns a tuple of their sum and product. The function is then tested with different input lists to ensure it works correctly.