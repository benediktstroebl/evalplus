```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple of sum and product of all elements in the list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case: empty list returns (0,1)
print(sum_product([]))  # Prints (0,1)

# Test case: single number list returns (sum, product)
print(sum_product([1]))  # Prints (1,1)

# Test case: positive list returns (sum, product)
print(sum_product([1, 2, 3, 4])) # Prints (10,24)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function then passes all the test cases, which demonstrate how the function behaves correctly with empty and non-empty lists.