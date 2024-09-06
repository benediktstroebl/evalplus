```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with various inputs
test_case_1 = [1, 2, 3]
test_case_2 = [10, 2, 3, 4]
test_case_3 = [1, 2, 3, 4, 5]
test_case_4 = [1, 2, 3, 6]

results = []
for test_case in test_case_1:
    result = sum_product(test_case)
    results.append(result)

for test_case in test_case_2:
    result = sum_product(test_case)
    results.append(result)

for test_case in test_case_3:
    result = sum_product(test_case)
    results.append(result)

for test_case in test_case_4:
    result = sum_product(test_case)
    results.append(result)

print(results)
```