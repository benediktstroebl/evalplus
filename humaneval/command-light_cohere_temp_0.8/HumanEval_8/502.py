Here is a self-contained Python function that solves the problem you provided:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Testing the function with known good inputs
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
assert result == (4, 24)

# Testing the function with an empty list
empty_list = []
result = sum_product(empty_list)
assert result == (0, 1)
```
This function takes a list of integers and returns a tuple consisting of a sum and a product of all the integers in the list. The function handles type annotations and returns a tuple with the sum and product values. 
It is then tested with two different inputs: a list of integers, and an empty list. The output values are then verified using asserts to ensure the correctness of the function's output.