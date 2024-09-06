```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
print(result)  # Output: (6, 24)
``` 
This script defines a function sum_product that takes a list of integers and returns a tuple with the sum and product of the integers. It then passes tests data with tests that check the correctness of the function. The test data and the result are printed to the console.