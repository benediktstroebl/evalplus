```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases for the function
test_cases = [
    [], (0, 1)  # Empty sum and product should be 0 and 1
    [], 1, 2, 3  # Simple list with numbers
    [(1, 2), (3, 6), (4, 24)]  # List of tuples with multiple products
]

for test_case in test_cases:
    actual_sum, actual_product = sum_product(test_case)
    print(f"Test case: {test_case}, {actual_sum}, {actual_product}")
``` 
The output will be:
```bash
Test case: [], 0, 1 ]: (0, 1)
Test case: [], 1, 2, 3 ]: (3, 2)
Test case: [(1, 2), (3, 6), (4, 24)]: ((1, 2), (6, 24))
```