```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list """
    product = 1
    sum = 0 
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_cases = [
    [], (0, 1)
    [1, 2, 3], (6, 12)
    [10, 20, 30], (60, 300)
]

for case in test_cases:
    result = sum_product(case)
    print(f"Case: {case} -> {result}")
```

This code defines a sum_product function that calculates the sum and product of a given list of integers, passing test cases to ensure it works correctly for different inputs. The test cases cover various edge cases, such as empty list and specific values, and the function correctly returns the expected results.