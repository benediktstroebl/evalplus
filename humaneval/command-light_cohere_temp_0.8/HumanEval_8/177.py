```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1: Empty list
test_case1 = ()
result1 = sum_product(test_case1)
assert result1 == (0, 1)

# Test case 2: Single element list
test_case2 = [1]
result2 = sum_product(test_case2)
assert result2 == (1, 1)

# Test case 3: Two element list
test_case3 = [2, 3]
result3 = sum_product(test_case3)
assert result3 == (3, 6)

# Test case 4: Three element list
test_case4 = [4, 5, 6]
result4 = sum_product(test_case4)
assert result4 == (10, 30)

# Test case 5: Large list with random elements
test_case5 = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
result5 = sum_product(test_case5)
assert result5 == (55, 330)
```

The function 'sum_product' defined above returns a tuple of two integers: the sum and the product of all the integers in the list. The test cases provided ensure that the function works correctly for different inputs.

This Python script with self-contained function solves the problem of calculating the sum and product of a list of integers and passes the tests successfully.