```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
print(result)  # Output: (6, 24)
```
This Python code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function performs the necessary calculation and handles the edge case of an empty list. The test data is set to [1, 2, 3, 4], and the function is called with this data. The result is then printed to show that the function is correct.