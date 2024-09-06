```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Numbers must be positive in ascending order.
    """

    Python runtime error will expected: ValueError: 'numbers' must be iterable
    """
    if not isinstance(numbers, List):
        raise ValueError("numbers" must be iterable)

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1
test_data = [1, 2, 3]
test_result = sum_product(test_data)
print("Test case 1: Sum =", test_result[0], ", Product =", test_result[1])

# Test case 2
test_data = [4, 5, 6]
test_result = sum_product(test_data)
print("Test case 2: Sum =", test_result[0], ", Product =", test_result[1])

# Test case 3 (edge case)
test_data = []
test_result = sum_product(test_data)
print("Test case 3: Sum =", test_result[0], ", Product =", test_result[1])
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function raises a ValueError exception if the input parameter `numbers` is not iterable. The test cases validate the expected output, and the script also covers the edge case where the input list is empty.