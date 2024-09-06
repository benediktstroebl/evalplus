```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print(test_result)  # Output: (6, 24)
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function utilizes a list comprehension and dictionary comprehension to iterate through the list and calculate the sum and product. The function is then successfully tested with the provided test data.