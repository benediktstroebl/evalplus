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
test_data = [0, 1]
test_result = sum_product(test_data)
print("Test Case 1: Result:", test_result)

test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print("Test Case 2: Result:", test_result)

test_data = [1, 2, 3]
test_result = sum_product([1, 2, 3])
print("Test Case 3: Result:", test_result)
```

The code defines a `sum_product` function that calculates the sum and product of a list of integers. It also includes several test cases to demonstrate the function's behavior. The output of the code would provide the results for the test cases.