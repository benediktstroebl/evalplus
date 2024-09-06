```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), prod(numbers))


def prod(numbers: List[int]) -> int:
    """Returns the product of the numbers in the list."""
    result = 1
    for number in numbers:
        result *= number
    return result

# Tests
numbers_list = [1, 2, 3, 4, 5]
result_sum, result_product = sum_product(numbers_list)
print(f"The sum is: {result_sum} and the product is: {result_product}")
``` 

To ensure that the function handles non-empty and empty lists correctly, two tests are included in the script. 

The `prod` helper function is also introduced to calculate the product of a list of numbers, which avoids recursion and is more efficient. 

To run the tests, simply insert the `numbers_list` variable with the desired list of numbers and execute the script. The sums and products will be printed accordingly. 
If there is any specific list you would like to test, feel free to add it to numbers_list variable and it will be included in the test.