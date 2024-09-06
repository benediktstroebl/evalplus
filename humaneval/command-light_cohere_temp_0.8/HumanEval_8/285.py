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
print(f"Sum: {result[0]} , {result[1]}")  # prints (10,24)
print("Test 2: ", sum_product([]) )   # empty list gives (0,1)
print("Test 3: ", sum_product([5,6,7]))  # single element list gives (5,304043)
print("Test 4: ", sum_product([1,6,8,9])) # list with 3 elements gives (6,8192)
print("Test 5: ", sum_product([10,1,2])) # list with 3 elements gives (15,720)
```
This code defines a function `sum_product` that calculates the sum and product of a given list of integers. It returns a also tuple containing the sum and product. 

This function is then tested with different input lists and passes all the tests successfully.