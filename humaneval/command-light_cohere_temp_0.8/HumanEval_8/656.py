```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in the list.
    Args: numbers (List[int]): A list of integers
    Returns: Tuple[int, int]: A tuple containing the sum and product of the numbers in the list
    """
    return (sum(numbers), product(numbers))

# Unit tests
def test_sum_product():
    test_list = [1, 2, 3, 4, 5]
    result = sum_product(test_list)
    assert result == (15, 120)  # This will fail if the function doesn't work as expected

if __name__ == "__main__":
    print("Testing sum_product function...")
    test_sum_product()
```
This Python script provides a self-contained function `sum_product` that calculates the sum and product of a given list of integers. It also includes unit tests to ensure the function behaves correctly.  The tests pass the example values to the function and verify the returned tuple matches the expected result. 

The `test_sum_product` function contains the unit tests.  The main function is used to run the tests when the script is executed.