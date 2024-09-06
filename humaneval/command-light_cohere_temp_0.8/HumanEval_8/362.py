```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Compute the sum and product of all integers in the list.
    Args: 
    - numbers (List[int]): list of integers 
    Returns: 
    - tuple(sum(numbers), product(numbers)) 
    """
    if not numbers: # handle empty list
        return (0, 1)
    return (sum(numbers), product(numbers))

# Unit tests
numbers = [1, 2, 3, 4, 5]
test_sum_product = sum_product(numbers)
print(test_sum_product)  # prints (15, 30)
```