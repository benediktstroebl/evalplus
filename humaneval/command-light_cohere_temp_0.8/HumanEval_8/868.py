Here's a self-contained Python script that defines a function sum_product that calculates and returns the sum and product of all integers in a list:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)

# Test case 1: empty list
test_case_1 = sum_product([])
assertEqual(test_case_1, (0, 1))

# Test case 2: single element list
test_case_2 = sum_product([1])
assertEqual(test_case_2, (1, 1))

# Test case 3: simple list
test_case_3 = sum_product([1, 2, 3])
assertEqual(test_case_3, (6, 12))

# Test case 4: large numbers list
test_case_4 = sum_product([5, 6, 7, 8])
assertEqual(test_case_4, (28, 56))
```
The provided code defines a function `sum_product` that calculates the sum and product of integers in a list. The `typing` module is used to add type hints to the function parameters and return values. The test cases cover various scenarios, including an empty list, a single element list, a simple list, and a large list of numbers, and verify the function's output and behavior.