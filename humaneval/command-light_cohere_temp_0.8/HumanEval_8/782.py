```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1
test_case_1 = [1, 2, 3, 4]
result_1 = sum_product(test_case_1)
assert result_1 == (4, 12)

# Test case 2
empty_list = []
result_2 = sum_product(empty_list)
assert result_2 == (0, 1)

# Test case 3
large_numbers = [65, 266, 9, 3]
result_3 = sum_product(large_numbers)
assert result_3 == (182, 233)
```
This Python script defines a function called `sum_product` that takes a list of integers as an argument and returns a tuple containing the sum and product of the integers in the list. The function utilizes a loop to calculate the sum and product of the numbers in the list. The test cases provided in the code aim to validate the correctness of the `sum_product` function by passing the test cases and asserting the corresponding results.