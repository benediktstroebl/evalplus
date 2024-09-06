```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function with valid input
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
print("Sum:", result)
print("Product:", result[1])

# Test the function with invalid input (empty list)
empty_list = []
result = sum_product(empty_list)
print("Sum:", result)
print("Product:", result[1])

``` 
This code includes a sum_product function that takes a list of integers as an input and returns a tuple with the sum and product of the integers. It is then pass several tests with both valid and invalid inputs.