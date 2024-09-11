```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple of the sum and product of the integers in the list.
    """
    sum_of_numbers = 0  # Initialize sum to 0
    product_of_numbers = 1  # Initialize product to 1

    for number in numbers:
        sum_of_numbers += number  # Add each number to the total sum
        product_of_numbers *= number  # Multiply each number with the total product

    return sum_of_numbers, product_of_numbers  # Return the sum and product as a tuple


# Test the function
if __name__ == "__main__":
    print(sum_product([]))  # Expected output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines the `sum_product` function as required, and then tests it with the provided test cases. The function works by initializing the sum and product to 0 and 1, respectively, and then iterating over the list of numbers, adding each number to the sum and multiplying each number with the product. Finally, it returns the sum and product as a tuple.