### Sum and Product of a List of Integers

The following Python script defines a function `sum_product` that calculates the sum and product of a given list of integers. It returns a tuple where the first element is the sum and the second element is the product.

```markdown
### Code
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
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num

    # Return the total sum and total product as a tuple
    return total_sum, total_product

### Example Usage
numbers1 = []
numbers2 = [1, 2, 3, 4]

# Calculate sum and product for each list
result1 = sum_product(numbers1)
result2 = sum_product(numbers2)

# Print the results
print(f"Sum and Product for empty list: {result1}")
print(f"Sum and Product for list [1, 2, 3, 4]: {result2}")
```

### Explanation

*   The `sum_product` function takes a list of integers as input and initializes the sum and product to 0 and 1 respectively.
*   It then iterates over each number in the list, adding the current number to the total sum and multiplying the current number with the total product.
*   Finally, it returns the total sum and total product as a tuple.
*   In the example usage, we demonstrate how to use the `sum_product` function for an empty list and a list containing the integers 1, 2, 3, and 4.