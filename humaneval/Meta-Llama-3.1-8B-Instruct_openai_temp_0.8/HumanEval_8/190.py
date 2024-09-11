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
    # Initialize sum and product variables with default values
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num
    
    # Return the calculated sum and product as a tuple
    return total_sum, total_product

# Test cases
if __name__ == "__main__":
    print(sum_product([]))  # Output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This Python script defines a function `sum_product` that calculates the sum and product of a given list of integers. It initializes `total_sum` to 0 and `total_product` to 1, then iterates over each number in the input list, updating `total_sum` by adding the current number and `total_product` by multiplying it with the current number. Finally, it returns the calculated sum and product as a tuple.

The script includes test cases to verify the function's correctness. When you run this script, it will print the expected output for the provided test cases.