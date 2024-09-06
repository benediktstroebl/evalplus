```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with some examples
numbers1 = [1, 2, 3, 4]
result1 = sum_product(numbers1)
print("Result 1:", result1)

numbers2 = []
result2 = sum_product(numbers2)
print("Result 2:", result2)

numbers3 = [5, 6, 7, 8]
result3 = sum_product(numbers3)
print("Result 3:", result3)
```
This function takes a list of integers as input and returns a tuple containing their sum and product. The function also provides a test cases to ensure its correctness.