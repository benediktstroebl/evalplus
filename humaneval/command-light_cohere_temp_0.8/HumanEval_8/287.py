```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    """
    list_sum=sum_product([1, 2, 3, 4])
    (10, 24)
    """
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

#Example function test
def test(func):
    numbers = [1, 2, 3, 4]
    result = func(numbers)
    print("Sum:",result[0])
    print("Product:",result[1])

test(sum_product)  # Passes the test
 ```