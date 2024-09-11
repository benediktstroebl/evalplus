```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Initialize sum and product with the default values
    total_sum = 0
    total_product = 1

    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        
        # Multiply the current number with the total product
        total_product *= num

    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test cases
def test_function():
    # Test case 1: Empty list
    assert sum_product([]) == (0, 1)
    
    # Test case 2: List with elements
    assert sum_product([1, 2, 3, 4]) == (10, 24)

# Run test cases
test_function()
```

This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a loop to iterate over each number in the input list, adding the current number to the total sum and multiplying the current number with the total product. The function then returns a tuple containing the total sum and product.

The script also includes test cases to verify the correctness of the `sum_product` function. The test cases use the `assert` statement to check if the function returns the expected results for different input scenarios.