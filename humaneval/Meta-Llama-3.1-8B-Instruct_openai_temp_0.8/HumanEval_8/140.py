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
    # Initialize sum and product to 0 and 1 respectively, as per the problem statement
    total_sum = 0
    product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        product *= num

    # Return a tuple containing the sum and product
    return total_sum, product


# Test the function
if __name__ == "__main__":
    print(sum_product([]))  # Output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

In this script, we define the `sum_product` function which takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. The function initializes sum and product to 0 and 1 respectively and then iterates over each number in the list, adding it to the sum and multiplying it with the product. Finally, it returns a tuple containing the sum and product.

We also include some test cases in the `if __name__ == "__main__":` block to verify that the function works as expected.