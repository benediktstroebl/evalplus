```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of integers in a list.
    if not numbers:  # Check for an empty list
        return (0, 1)
    elif len(numbers) == 0:  # Test case for a single element list
        return (numbers[0], numbers[0]*numbers[0])
    else:
        product = 1
        sum = 0
        for num in numbers:
            product *= num
            sum += num
        return (sum, product)
```