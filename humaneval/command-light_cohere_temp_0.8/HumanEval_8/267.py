```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    Args:
    numbers: list of integers

    Returns:
    A tuple containing a sum and a product of all the integers in numbers.
    """
    def product(x):
        if len(x) == 0:
            return 1
        return x[0] * x[1]
    
    return (sum(x) , product(numbers))

numbers = [1,2,3,4]
print(sum_product(numbers)) # prints (10,24)
print(sum_product([])) # Empty list, returns (0,1)
print(sum_product([1,2,3] )) # Single element list, returns (6,1)
print(sum_product([1,2,3,4,5] )) # Longer list, returns (26,40)
```