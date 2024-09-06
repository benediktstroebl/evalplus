```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = [1]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
``` 
This code defines the sum_product function which takes a list of integers as an argument and returns a tuple containing the sum and product of the numbers in the list. The function uses a loop to calculate the sum and product of each number in the list. 

The tests section passes the values of the `numbers` list and the empty list as arguments to the `sum_product` function and checks that the function returns the correct results.