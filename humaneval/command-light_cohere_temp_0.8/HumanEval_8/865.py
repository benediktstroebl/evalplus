```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of the integers in the list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
test_sum_product = [
    [
        ((), 0),
        ([], 1),
        ([1, 2, 3], 6),
        ([1, 2, 3, 4], 24),
    ]
]

def test_function(test_case: Tuple[List[int]]) -> None:
    """ Test function, checks if the output of sum_product matches the expected output """
    assert sum_product(test_case[0]) == test_case[1]
    return "Pass"

# Example usage
test_sum_product = [
    ((), 0),
    ([], 1),
    ([1, 2, 3], 6),
    ([1, 2, 3, 4], 24),
]
test_function(test_sum_product)  # Should print "Pass"
 ```