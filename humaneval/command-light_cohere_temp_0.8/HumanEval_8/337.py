```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Test for empty list
        return (0, 1)
    
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function
test_result = sum_product([1, 2, 3, 4])
print(test_result)  # Output: (10, 24)
 ```