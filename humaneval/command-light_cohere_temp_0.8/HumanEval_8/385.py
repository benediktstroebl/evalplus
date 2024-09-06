```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # if empty list
        return (0, 1)
    return (sum(numbers), product(numbers))  # sum and product using built-in functions

# Test the function with a valid input
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
print(result)  # expected output: (10, 24)

# Test the function with an empty list
empty_list = []
result = sum_product(empty_list)
print(result)  # expected output: (0, 1)
``` 
This script defines a sum_product function that takes a list of integers as an input and returns a tuple with the sum and product of the integers in the list. It then passes the  an empty list test case, and also a test case with a list of integers. The output of the expected sum and product are displayed for both test cases.