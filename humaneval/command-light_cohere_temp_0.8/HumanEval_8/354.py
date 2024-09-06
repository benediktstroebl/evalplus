```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers1 = [1, 2, 3]
result1 = sum_product(numbers1)
print("Result 1:", result1)

numbers2 = []
result2 = sum_product(numbers2)
print("Result 2:", result2)

numbers3 = [10, 2, 3]
result3 = sum_product(numbers3)
print("Result 3:", result3)
```
The code defines the `sum_product` function that calculates the sum and product of the integers in a given list. The function uses a simple loop to iterate through the list and update the running product and sum. The test cases demonstrate how the use the function with different lists of integers and empty lists.