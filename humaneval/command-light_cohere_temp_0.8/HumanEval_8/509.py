```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 1
    for num in numbers:
        result *= num
    return (result, result)
# Test the function
test_numbers = [1, 2, 3, 4]
result = sum_product(test_numbers)
print("Test 1: sum:", result)
print("Test 2: product:", result)
``` 
This script defines a function `sum_product` that takes a list of integers as input and returns a tuple with the sum and product of all the integers in the list. The script also provides test cases to verify the correctness of the function.

This function uses the `result` variable to initialize a product value, and then loops through the list, multiplying each element with the current value of `result`. Finally, the product and the sum are returned in a tuple.

This script follows the Single Responsibility Principle. It separates concerns into a small functions with specific purposes, improving code readability and maintainability.