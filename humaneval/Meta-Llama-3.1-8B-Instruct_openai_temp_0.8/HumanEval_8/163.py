```markdown
### Sum and Product of a List of Integers

This script defines a function `sum_product` that calculates the sum and product of a given list of integers.

#### Code

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    # Handle the edge case where the list is empty
    if not numbers:
        return 0, 1
    
    # Initialize sum and product variables
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers and calculate the sum and product
    for num in numbers:
        total_sum += num
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function with some examples
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

#### Explanation

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function first handles the edge case where the input list is empty, in which case it returns a tuple with a sum of 0 and a product of 1. It then initializes variables to keep track of the sum and product, and iterates over the list of numbers, updating these variables as it goes. Finally, it returns the sum and product as a tuple.

Note that this implementation has a time complexity of O(n), where n is the length of the input list, since it involves a single pass over the list. The space complexity is O(1), since it only uses a constant amount of space to store the sum and product variables.