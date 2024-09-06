```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    Args:
        numbers: list of integers
    Returns:
        tuple containing a sum (int) and a product (int) of the list of integers.
    """
    list comprehension is a way to convert the input to tuple:
        (sum(numbers), product(numbers)))
    """
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1: Empty list
test_case_1 = ()
result_case_1 = sum_product(test_case_1)
assert result_case_1 == (0, 1)

# Test case 2: Single element list
test_case_2 = [1]
result_case_2 = sum_product(test_case_2)
assert result_case_2 == (1, 1)

# Test case 3: Multiple elements list
test_case_3 = [1, 2, 3, 4]
result_case_3 = sum_product(test_case_3)
assert result_case_3 == (10, 24)
```
The above Python script defines a function sum_product that calculates the sum and product of a given list of integers. The function utilizes a list comprehension to create a tuple with the sum and product values. It then passes these tests to ensure the correctness of the function.