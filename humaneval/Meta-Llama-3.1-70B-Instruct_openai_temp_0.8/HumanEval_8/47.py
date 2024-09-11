```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple of sum and product of the integers in the list.
    """
    # Initialize sum and product with the identity values for empty lists
    total_sum = 0
    total_product = 1

    # Iterate over the list of numbers
    for number in numbers:
        # Add the current number to the sum
        total_sum += number
        # Multiply the current number with the product
        total_product *= number

    # Return the sum and product as a tuple
    return total_sum, total_product


def main():
    # Test cases
    print(sum_product([]))  # Expected output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)


if __name__ == "__main__":
    main()
```

Alternatively, you can use the built-in `sum` function and `math.prod` function (available in Python 3.8+) to make the code more concise:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple of sum and product of the integers in the list.
    """
    # Use the sum function for calculating the sum
    total_sum = sum(numbers)
    # Use the prod function for calculating the product, defaulting to 1 for empty lists
    total_product = math.prod(numbers, start=1)

    # Return the sum and product as a tuple
    return total_sum, total_product


def main():
    # Test cases
    print(sum_product([]))  # Expected output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)


if __name__ == "__main__":
    main()
```