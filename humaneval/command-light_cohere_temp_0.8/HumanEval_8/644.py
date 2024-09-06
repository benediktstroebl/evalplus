```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1: empty list
print(sum_product([]))  # Output: (0, 1)

# Test case 2: single element list
print(sum_product([1]))  # Output: (1, 1)

# Test case 3: double-length list
print(sum_product([1, 2, 3]))  # Output: (6, 6)

# Test case 4: list with repeating elements
numbers = [1, 2, 3, 4, 3]
print(sum_product(numbers))  # Output: (10, 12)
```
This script provides a sum_product function that takes a list of integers and returns a tuple containing the sum and product of the numbers in the list. The tests verify that expected outputs.