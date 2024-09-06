```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # test for empty list
        return (0, 1)
    
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# test the function
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print(test_result)  # prints (6, 24)
``` 
This Python code defines a function called sum_product that takes a list of integers as input and returns a tuple of their sum and product. The function first handles an edge case of an empty list, returning (0, 1) in such cases.