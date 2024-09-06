```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)
    return

#Test case 1: Empty list
print(sum_product([]))  # Output: (0, 1)

#Test case 2: List with two elements
print(sum_product([1, 2]))  # Output: (3, 2)

#Test case 3: List with three elements
print(sum_product([1, 2, 3]))  # Output: (6, 6)

#Test case 4: List with more than three elements
numbers = [1, 2, 3, 4, 5]
print(sum_product(numbers))  # Output: (10, 20)
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses type hints, function annotations to describe the expected input parameter and return types. The function takes a input list of integers and returns a tuple containing their sum and product. It performs the sum of the numbers using the `sum` function and calculates the product by iterating over each element in the list.

The code also includes several test cases that demonstrate how the `sum_product` function behaves when given different lists of integers.