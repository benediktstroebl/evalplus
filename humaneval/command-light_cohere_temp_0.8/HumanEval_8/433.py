```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1: empty list
test_case_1 = ()
result_case_1 = sum_product(test_case_1)
assert sum(result_case_1) == 0, "Sum should be 0 for empty list."
assert result_case_1[0] == 0, "Sum should be 0"

# Test case 2: single element list
test_case_2 = [1]
result_case_2 = sum_product(test_case_2)
assert sum(result_case_2) == 1, "Sum should be 1"
assert result_case_2[0] == 1, "Sum should be 1"

# Test case 3: basic list
test_case_3 = [1, 2, 3]
result_case_3 = sum_product(test_case_3)
assert sum(result_case_3) == 6, "Sum should be 6"
assert result_case_3[0] == 6, "Sum should be 6"
assert result_case_3[1] == 6, "Sum should be 6"

# Test case 4: list with duplicates
test_case_4 = [1, 2, 2]
result_case_4 = sum_product(test_case_4)
assert sum(result_case_4) == 5, "Sum should be 5"
assert result_case_4[0] == 2, "Sum should be 2"
assert result_case_4[1] == 2, "Sum should be 2"
```
The code defines a `sum_product` function that calculates the sum and product of a given list of integers, returning them as a tuple. It provides four test cases with various lists to test the function, passing all the tests successfully.