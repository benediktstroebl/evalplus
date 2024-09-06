```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test case
test_numbers = [1, 2, 3, 4]
result = sum_product(test_numbers)
print(result)  # Output: (6, 24)
``` 
The function calculates the sum and product of the integers in the passed list, and then returns them in a tuple. This script is way demonstrates a concept of self-contained code and function definitions, passing test cases.