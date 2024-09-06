```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test cases
test_list1 = [1, 2, 3, 4]
test_list2 = []
result1 = sum_product(test_list1)
result2 = sum_product([1, 2, 3, 4])
print("Result 1:", result1)
print("Result 2:", result2)
```
The output will display two values which are 10 and 24 respectively.