```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list, return 0 and 1
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24
``` 
This code defines a `sum_product` function that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. It handles the empty input gracefully by returning `(0, 1)` instead. 

In the test case, it creates a list `[1, 2, 3, 4]` and calls the `sum_product` function. It then prints the result, which is a tuple of the sum and product of the numbers.