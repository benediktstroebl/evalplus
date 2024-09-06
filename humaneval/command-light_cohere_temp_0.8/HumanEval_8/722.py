```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit Tests
test_sum_product = [
    ( [1, 2, 3, 4],     # List with 4 integers
        (10, 24),           # Expected return: (10, 24)
        ),
]

if __name__ == "__main__":
    test_sum_product = test_sum_product[0]
    actual_result = sum_product(test_sum_product)
    assert actual_result == test_sum_product[1]
``` 
This Python code defines a function sum_product that calculates the sum and product of a list of integers. The function uses a product variable to initialize a product value of 1, and the sum variable to keep track of the sum of the numbers. The function then iterates over each element in the list, multiplying each number with the product, and adding each number to the sum. The resulting tuple is (sum, product). The unit tests test this function by providing a list of integers with specific values and the expected return values. The test passes successfully when the actual result matches the expected return.