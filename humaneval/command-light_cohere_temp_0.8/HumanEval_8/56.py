```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of integers in numbers list """
    total_sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (total_sum, product)
def test_sum_product():
    """ Test the sum_product function by providing test cases """
    numbers = [1, 2, 3, 4, 5]
    result = sum_product(numbers)
    assert result == (15, 120)
    numbers = []
    result = sum_product(numbers)
    assert result == (0, 1)
    numbers = [10, 20, 30, 40]
    result = sum_product(numbers)
    assert result == (50, 3000)
test_sum_product()  # test suite execution if the function is defined in main() or an exec statement
``` 
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers, and passes tests using test cases. The test suite includes testing the both with empty lists and lists of specific numbers, as well as edge cases where no elements in the input list.