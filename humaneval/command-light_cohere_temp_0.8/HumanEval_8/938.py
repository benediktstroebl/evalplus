```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:  # if an empty list is passed in
        return (0, 1)
    elif len(numbers) == 0:
        return (0, 0)
    else:
        product = 1
        sum = 0
        for num in numbers:
            product *= num
            sum += num
        return (sum, product)
    ```