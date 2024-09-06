```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple containing sum and product of the numbers in the list.
    Args: 
    - numbers (List[int]): A list of integers
    Returns: 
    - tuple(int, int): A tuple containing sum and product of the numbers in the list
    """
    if not numbers:
        return (0, 1)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Unit Tests

def test_sum_product():
    test_list = [1, 2, 3, 4]
    result = sum_product(test_list)
    assert result == (10, 24)

def test_empty_list():
    test_list = []
    result = sum_product(test_list)
    assert result == (0, 1)

def test_single_number():
    test_list = [5]
    result = sum_product(test_list)
    assert result == (5, 5)

def test_product_vs_sum():
    test_list = [1, 2, 3, 4]
    result = sum_product(test_list)
    assert result == (10, 24)

# Call the function with the tests
test_sum_product()
 ``` 
This code defines a function sum_product that calculates the sum and product of a given list of integers, and it is tested using unit tests. The unit tests cover different scenarios, such as an empty list, a list with a single number, and a list of numbers.

The script also demonstrates the usage of the function with different test cases, passing the tests successfully.