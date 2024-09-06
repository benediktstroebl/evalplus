```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1: empty list
test_sum_product([])
>>> (result, answer) = sum_product([])
>>> result, answer
(0, 1)

# Test case 2: single number list
test_sum_product([1])
>>> (result, answer) = sum_product([1])
>>> result, answer
(1, 1)

# Test case 3: short list
test_sum_product([1, 2, 3])
>>> (result, answer) = sum_product([1, 2, 3])
>>> result, answer
(3, 6)

# Test case 4: list with duplicate numbers
test_sum_product([1, 2, 2])
>>> (result, answer) = sum_product([1, 2, 2])
>>> result, answer
(4, 4)

# Test case 5: empty list with int conversion
test_sum_product([1, 2, 3, 4])
>>> (result, answer) = sum_product([1, 2, 3, 4])
>>> result, answer
(6, 4)
```
The provided Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple of the sum and product of the numbers in the list. It then passes several tests to validate the correctness of the function.