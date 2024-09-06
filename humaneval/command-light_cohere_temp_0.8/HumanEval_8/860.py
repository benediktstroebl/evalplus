```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# pass the test
print(sum_product([1, 2, 3, 4]))
``` 
The above function uses the loop to iterate through the list of numbers, then multiplies all the numbers together and adds all the numbers. The product of all the numbers is stored in the product variable, and the sum of all the numbers is stored in the sum variable.