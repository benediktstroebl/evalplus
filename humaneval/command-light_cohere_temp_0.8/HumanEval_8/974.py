```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: empty list
test_sum_product([]) -> (0, 1)  # Should return (0, 1)

# Test case 2: single element list
test_sum_product([1]) -> (1, 1)  # Should return (1, 1)

# Test case 3: simple list
test_sum_product([1, 2, 3, 4]) -> (10, 24)  # Should return (10, 24)

# Test case 4: duplicate elements
test_sum_product([1, 2, 2, 3]) -> (11, 6)  # Should return (11, 6)

# Test case 5: large list with large numbers
test_sum_product([1000, 5000, 1000]) -> ( 3000, 3000000)  # Should return (3000, 3000000)
```
This code defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the list elements. The function first handles an edge case of an empty list and returns (0, 1), and in all other cases, it calculates the sum and product of the numbers in the list and returns the result.