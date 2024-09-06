```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of integers in a list.
    Input: A list of integers.
    Output: A tuple consisting of sum and product of the integers in the list.
    """
    empty sum should be equal to 0 and empty product should be 1.
    Return a return a tuple containing sum and product values.
    """
    list is the sum of numbers, multiplied by product of all numbers in the list.
    """return (sum(numbers), product(numbers))
    """

def test_sum_product():
    """
    Test case 1: Test empty list.
    """
    input():
        []
    assert sum_product([]) == (0, 1)

    """
    Test case 2: Test list with one element.
    """
    input():
        [5]
    assert sum_product([]) == (0, 5)

    """
    Test case 3: Test list with multiple elements.
    """input numbers=[1, 2, 3, 4]
    assert sum_product(numbers) == (3, 12)

    """
    Test case 4: Test list with duplicate elements.
    """input numbers=[1, 1, 2, 2, 3, 4, 4]
    assert sum_product(numbers) == (6, 20)

    """
    Test case 5: Test list with large numbers.
    """input numbers=[1000000, 2000000, 3000000]
    assert sum_product(numbers) == (3, 600000)

    """
test_sum_product()
```