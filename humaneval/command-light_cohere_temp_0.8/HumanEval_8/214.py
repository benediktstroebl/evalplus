```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of a given list of integers.
    Args:
        numbers: list of integers
    
    Returns:
        tuple: consisting of a sum and a product of all the integers in the list
    """
    if not numbers:
        return (0, 1)
    
    product = 1
    sum_ = 0
    for num in numbers:
        product *= num
        sum_ += num
    return (sum_, product)

# Test case
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print("Test case 1 result:", test_result)  # Output: (6, 24)

# Another test case
test_data2 = [5, 6, 7]
test_result2 = sum_product(test_data2)
print("Test case 2 result:", test_result2)  # Output: (20, 210)
``` 
This code defines a `sum_product` function that calculates the sum and product of a list of integers. The function returns a result as a tuple with the sum and product. The `test_data` variable is passed as an argument to the `sum_product` function to test the function with two sets of integers.

This code is self-contained, and it can be copied and pasted into a Python environment and run without needing external code.