```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of the integers in the list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1
test_case1 = [1, 2, 3, 4]
result1 = sum_product(test_case1)
print("Result 1:", result1)

# Test case 2: empty list
test_case2 = []
result2 = sum_product(test_case2)
print("Result 2:", result2)
```
The function `sum_product` takes a list of integers as input and returns a tuple with the sum and product of the integers in the list. The test cases demonstrate the general functionality of the function.