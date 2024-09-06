```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
#Test cases
test_cases = [(), 1, 2, 3, 4]
result = sum_product(test_cases)
print(result)
``` 
This code provides a function sum_product that calculates the sum and product of a list of integers. The function is designed to handle both empty input and various numbers of the list. The return a sum should be calculated by summing each element and the product should be calculated by multiplying each element in the list.