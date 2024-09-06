```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple of sum and product of integers in the list """
    product = 1
    sum = 0 
    for num in numbers:
        product *= num
        sum += num 
    return (sum, product)
# Test the function
numbers = [1, 2, 3, 4]
test_result = sum_product(numbers)
print(test_result)  # Output: (6, 24)
```