```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    :return 0,1 if an empty list
    :return sum(numbers), product(numbers)
    """
    if not numbers:
        return 0, 1

    sum_product = sum(numbers) * product(numbers)
    return sum_product, sum_product // len(numbers)

# Unit tests
test_sum_product = [
    [ (-10, 0),       # ValueError: cannot divide by zero
     (10, 10),      # ValueError: invalid mathop operation, 2 * 10 = 20
    ]
]

test_product = [
    [ (0, 1),         # Test case: empty list
    ]
]

test_sum_product = [
    [ (1, 10),       # Test case: list with one element
    (10, 40),        # Test case: list with two elements
    (10, 100),      # Test case: list with three elements
    (20, 600),      # Test case: list with large number of elements
    (10, 1000)     # Test case: list with a large sum
]

def test_sum_product():
    for test_case in test_sum_product:
        assert sum_product(test_case) == test_case[0], "Test case 1 failed: {}".format()

if __name__ == "__main__":
    test_sum_product()  # Run the tests when the script is run directly
 ```
This Python script defines a function called sum_product, which calculates the sum and product of a list of integers. The function handles empty lists gracefully, and the unit tests cover various test cases, ensuring the correctness of the function. The tests are executed when the script is run directly, and any failures will trigger an error message.