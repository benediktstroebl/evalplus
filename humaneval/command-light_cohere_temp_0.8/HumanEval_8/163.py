```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of the list of integers """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with various lists of integers
test_data = [1, 2, 3, 4, 5]
test_result = sum_product(test_data)
print("Test 1:", test_result)  # Output: (6, 20)

test_data = []
test_result = sum_product(test_data)
print("Test 2:", test_result)  # Output: (0, 1)

test_data = [10, 20, 30]
test_result = sum_product(test_data)
print("Test 3:", test_result)  # Output: (60, 600)
```