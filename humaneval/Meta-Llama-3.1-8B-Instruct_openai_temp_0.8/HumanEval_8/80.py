```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in a list.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Initialize sum and product with default values for an empty list
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        
        # Multiply the current number with the total product
        total_product *= num
    
    # Return a tuple consisting of the total sum and the total product
    return total_sum, total_product


# Test the function
if __name__ == "__main__":
    print(sum_product([]))  # (0, 1)
    print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

In this script, we define the `sum_product` function, which calculates the sum and product of all numbers in a given list. The function initializes the sum and product with default values (0 and 1, respectively) and then iterates over the list, updating the sum and product at each step. Finally, the function returns a tuple consisting of the total sum and the total product. The script also includes test cases to demonstrate the function's behavior.