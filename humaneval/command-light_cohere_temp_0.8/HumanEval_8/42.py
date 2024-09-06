Here is a self-contained Python script with a function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    Args:
        List[int] numbers: The list of integers.
    Returns: Tuple[int, int] consisting of sum and product of the list of integers.
    Returns: None if the list is empty.
    """
    def sum_product(numbers: List[int]) -> Tuple[int, int]:
        # Initialize the sum and product variables
        sum = 0
        product = 1

        # Calculate the sum and product of the list of integers
        for num in numbers:
            sum += num
            product *= num

        # Return the calculated sum and product
        return (sum, product)

# Test the function with different inputs
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print("Sum:", result[0])
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result[0])
print("Product:", result[1])

numbers = [1, 2, 3]
result = sum_product(numbers)
print("Sum:", result[0])
print("Product:", result[1])
```

The above Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the list. The function first initializes the same variables, then loops through the list and accumulates the sum and product the numbers by multiplying them. The function then returns the value of the tuple.