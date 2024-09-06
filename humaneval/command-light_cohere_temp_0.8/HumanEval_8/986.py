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
result = sum_product(test_data)
print(f"Sum: {result[0]}  {result[1]}")
test_data.no difference in the different list.

``` 
This script defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. It is then tested using a list of numbers and the result is printed to the console.