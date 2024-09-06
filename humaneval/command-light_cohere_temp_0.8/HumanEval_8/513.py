```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Create list with random numbers
numbers = [4, 10, 2, 81, 3]
print(sum_product(numbers))  # Expected Output: (15, 144)
```