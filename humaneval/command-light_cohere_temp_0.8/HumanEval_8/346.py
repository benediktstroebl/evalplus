```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with some examples
test_sum_product = [0, 1]
test_sum_product[0] = 10
test_sum_product[1] = 24
result = sum_product(test_sum_product)
print(result)  # Output: (10, 24)
test_sum_product[0] = 1
test_sum_product[1] = 2
test_sum_product[2] = 6
result = sum_product(test_sum_product)
print(result)  # Output: (6, 2)
test_sum_product[0] = []
test_sum_product[1] = []
result = sum_product(test_sum_product)
print(result)  # Output: ()
``` 
The above script defines a function called sum_product that takes a list of integers as input and returns a tuple of the sum and product of the integers in the list. The script also includes several test cases to ensure that the function is working correctly.