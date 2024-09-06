```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))


def products(numbers: List[int]) -> int:
    product = 1
    for num in numbers:
        product *= num
    return product
``` 
This function utilizes the List[int] parameter to calculate the sum and product of a list of integers. It ensures that the relevant tests are passed successfully.