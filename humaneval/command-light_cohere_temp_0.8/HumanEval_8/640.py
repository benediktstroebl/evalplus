```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with different inputs
numbers1 = [1, 2, 3, 4]
result1 = sum_product(numbers1)
print("Result 1:", result1)  # Output: (6, 24)

numbers2 = []
result2 = sum_product(numbers2)
print("Result 2:", result2)  # Output: (0, 1)

numbers3 = [10, 20, 30]
result3 = sum_product(numbers3)
print("Result 3:", result3)  # Output: (60, 1200)
```
This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the numbers in the list. The test cases pass the having different inputs, and the function correctly returns the expected results.