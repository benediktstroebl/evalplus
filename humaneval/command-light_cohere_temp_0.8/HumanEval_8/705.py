```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list"""
    
    # Initialize result
    total_sum = 0
    product = 1

    # Iterate over list and calculate sum and product
    for num in numbers:
        total_sum += num
        product *= num

    return (total_sum, product)

# Unit tests
test_sum_product = [

    # Test empty list
    assert sum_product([]) == (0, 1), "Empty list should yield (0, 1)"

    # Test single number list
    assert sum_product([1]) == (1, 1), "List with a single number should yield (sum, product)"

    # Test list with multiple numbers
    assert sum_product([1, 2, 3, 4]) == (10, 24), "List with multiple numbers should yield (sum, product)"

# Main code execution
```