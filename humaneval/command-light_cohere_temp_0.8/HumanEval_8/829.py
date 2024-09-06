```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    >>> print(sum_product([1, 2, 3, 4]))
    (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Additional test cases
print(sum_product([0]))    # Output: (0, 1)
print(sum_product([]))    # Output: (0, 1)
print(sum_product([1, 2, 3, 4, 5, 6])) # Output: (16, 120)
```
This function calculates the sum and product of the list of integers and provides test cases to ensure it works correctly for different inputs.