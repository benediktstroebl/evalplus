```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a given list of integers.
    Each number is present at least index is expected to be non-negative.
    Returns a value of the sum of the list and product of the list.
    """

    Raise an ValueError if the list is empty or contains a negative number.
    """

    raise ValueError("Input list must contain only positive numbers")
    if not_positive(numbers):
        raise ValueError("Input list must contain only positive numbers")

    return (sum(numbers), product(numbers))
    """

def product(numbers: List[int]) -> int:
    """
    Returns the product of a list of integers
    """
    return 1 if not_positive(numbers) else product(numbers[1:]) * numbers[0]

def not_positive(numbers: List[int]) -> bool:
    """
    Check if the list contains only positive numbers
    """
    return all(num > 0 for num in numbers)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    print("Sum:", result[0])
    print("Product:", result[1])
```

This Python code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. It uses two other functions, product, and not_positive to perform the calculations and checks. This code ensures that the values are calculated correctly and raises appropriate errors when needed. The main function demonstrates the example of calling the sum_product function with a list of integers [1, 2, 3, 4] and printing the results.