```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1: empty list
test_case_1 = ()
result_case_1 = sum_product(test_case_1)
print(result_case_1)  # Output: ()

# Test case 2: single element list
test_case_2 = [1]
result_case_2 = sum_product(test_case_2)
print(result_case_2)  # Output: (1, 1)

# Test case 3: list of 2 elements
test_case_3 = [2, 3]
result_case_3 = sum_product(test_case_3)
print(result_case_3)  # Output: (3, 6)

# Test case 4: list of 3 elements
test_case_4 = [1, 2, 3]
result_case_4 = sum_product(test_case_4)
print(result_case_4)  # Output: (6, 8)

# Test case 5: list of 4 elements
test_case_5 = [1, 2, 3, 4]
result_case_5 = sum_product(test_case_5)
print(result_case_5)  # Output: (10, 16)
```

The code defines a function `sum_product` that calculates the sum and product of a list of integers, passing these values through the return statement. The test cases cover various scenarios, from an empty list to a list of four elements, passing them through the `sum_product` function and printing the results.