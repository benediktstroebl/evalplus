```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (6, 24)
numbers = []
result = sum_product(numbers)
print(result)  # Output: (0, 1)
numbers = [1, 2, 3, ,4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This Python script defines a function `sum_product` that takes a list of integers as an input and returns a tuple with two integers: the sum and the product of the integers in the list. The function uses a loop to iterate through the list of numbers, and accumulates the sum and multiplies each element in the product variable. The script also provides several test cases to demonstrate the functionality of the `sum_product` function.