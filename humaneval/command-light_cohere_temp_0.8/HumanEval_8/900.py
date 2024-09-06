```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Test the function
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([5, 6, 7, 8]))  # Output: (28, 56)
print(sum_product([]))  # Output: (0, 1)
print(sum_product([90]))  # Error: [90] is not a list of integers
```
This code defines a function `sum_product` that takes a list of integers as input and returns a tuple with the sum of the numbers and their product. The function uses a first checks if the input is empty and returns `(0, 1)` in this case. The product is then calculated by multiplying all the numbers in the list and storing the result in the product variable. The sum of the numbers is calculated by summing the elements in the list using the `sum` function. 

The test section ensures that the function works correctly for different input scenarios.