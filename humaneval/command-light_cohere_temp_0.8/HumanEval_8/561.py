```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1
test_case_1 = [1, 2, 3, 4]
print(sum_product(test_case_1))  # Output: (10, 24)

# Test case 2
test_case_2 = []
print(sum_product(test_case_2))  # Output: (0, 1)

# Test case 3
test_case_3 = [1, 2, 3]
print(sum_product(test_case_3))  # Output: (6, 6)
```

This Python script defines a function called sum_product that calculates the sum and product of a list of integers. It uses the `typing` to make sure that the function is self-contained and the parameters are correctly typed. The test cases ensure that the function works as expected for different inputs.