```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function with sample inputs
test_cases = [(0, 0), (1, 1), (2, 4), (5, 120), (3, 8), (10, 800)]
for case in test_cases:
    actual = sum_product(case)
    expected = case
    print(f"Case {case} : {actual}, Expected: {expected}")
    assert actual == expected
```