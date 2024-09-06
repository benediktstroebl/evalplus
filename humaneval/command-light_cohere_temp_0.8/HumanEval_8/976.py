```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
#Test cases
test_data = [1, 2, 3, 4]
test_results = sum_product(test_data)
print(test_results)  #Expected output: (6, 24)
``` 
This code defines the function **sum_product**, which accepts a list of integers and returns a tuple containing the sum and product of the integers in the list. It then defines a test cases using a list of numbers [1,2,3,4] and executes the sum_product function, resulting in the product (6,24) being printed.