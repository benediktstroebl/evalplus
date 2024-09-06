```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test the function with a valid input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24

# Test the function with an empty list
empty_numbers = []
result = sum_product(empty_numbers)
print("Sum:", result)  # Output: 0
print("Product:", result[1])  # Output: 1
```
The provided Python code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the integers. The function uses two variables: product to keep track of the product value and sum to store the sum. The function then iterates over each number in the input list, updating the product and sum variables accordingly. The test section follows, passing the function with valid input and then printing the returned sum and product values. The output will show the values of the sum and product for a valid input list, and for an empty list, respectively.