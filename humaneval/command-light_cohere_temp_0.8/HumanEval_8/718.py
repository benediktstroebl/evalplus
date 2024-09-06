Here's the solution to the problem you described: 

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in the list.
    Args: 
        numbers (List[int]): A list of integers.
    Returns:  A tuple of sum and product of all integers.
    """
    def sum_product(numbers: List[int]) -> Tuple[int, int]:
        product = 1
        sum = 0
        for num in numbers:
            product *= num
            sum += num
        return (sum, product)
    return sum_product
```

This function takes a list of integers as input and returns a tuple of two integers: the sum of all integers in the list and the product of all integers in the list.

It uses a for loop to iterate over each element in the list, multiplying each element with the product and adding it to the sum. 

The function then returns a tuple of the sum and the product.