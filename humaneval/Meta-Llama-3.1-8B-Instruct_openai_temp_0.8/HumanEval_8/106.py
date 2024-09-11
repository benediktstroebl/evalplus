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
    sum_result = 0  # Initialize sum result to 0
    product_result = 1  # Initialize product result to 1

    for num in numbers:
        # For each number in the list, add it to the sum result
        sum_result += num
        # For each number in the list, multiply it with the product result
        product_result *= num

    # Return a tuple containing the sum and product results
    return sum_result, product_result

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines a function `sum_product` that calculates the sum and product of a given list of integers. The function uses a for loop to iterate over each number in the list, updating the sum and product results accordingly. The function then returns a tuple containing the sum and product results. The script also includes test cases to demonstrate the function's behavior.