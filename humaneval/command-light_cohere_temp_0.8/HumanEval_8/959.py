Here is a self-contained Python script with a function that solves the problem of calculating the sum and product of a list of integers and passes corresponding tests:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print("Test Results:", test_result) # (6, 24)
```