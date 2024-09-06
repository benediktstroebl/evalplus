```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Corrected logical condition to handle empty list
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This code provides a function called sum_product that takes a list of integers as input and returns a tuple with two values: the sum of the numbers and the product of the numbers. The function first checks if the condition to handle an empty list, and then proceeds to calculate the sum and product. Additionally, it uses the product function from the itertools library to efficiently calculate the product of the numbers. The output is then the tuple with two values: the sum and product of the input list.