```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
``` 
This function performs the sum and product operation on a given list of integers. It iterates through elements in a list to calculate the sum and product and returns a tuple of these two values.