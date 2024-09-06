```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test cases
test_list1 = [1, 2, 3]
test_list2 = [4, 5, 6]
test_list3 = []
result1 = sum_product(test_list1)
result2 = sum_product(test_list2)
result3 = sum_product(test_list3)

if isinstance(result1, Tuple) and len(result1) == 2 and result1[0] == 6 and result1[1] == 6:
    pass
if isinstance(result2, Tuple) and len(result2) == 2 and result2[0] == 20 and result2[1] == 120:
    pass
if not isinstance(result3, Tuple) or not len(result3) == 2:
    print("Error: Incorrect input or function expects a list of integers.")
```