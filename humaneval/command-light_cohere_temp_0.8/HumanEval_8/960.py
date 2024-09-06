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
test_case1 = [1, 2, 3]
result1 = sum_product(test_case1)
print("Test case 1 result:", result1)

# Test case 2
test_case2 = [1, 2, 4]
result2 = sum_product(test_case2)
print("Test case 2 result:", result2)

# Test case 3
test_case3 = [1, 2, 3, 4]
result3 = sum_product(test_case3)
print("Test case 3 result:", result3)
```
This code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. It uses a nested loops to iterate through the list and accumulate the sum and product, respectively. The test cases are simple lists of integers that can be passed as input to the function and the expected output is printed for each test case.