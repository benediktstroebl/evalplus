```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
assert len(result) == 2
assert result[0] == 10
assert result[1] == 24
``` 
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It utilizes the type hint `List[int]` for the input parameter `numbers` to ensure that only integers are passed. The function also returns a tuple containing the sum and product of the numbers. The test case demonstrates the same approach, passing the function with test data and asserting that the function returns the correct result.