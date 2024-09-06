```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all integers in the list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test the function with sample inputs
test_list = [1, 2, 3, 4]
test_output = sum_product(test_list)
print(test_output)  # Output: (6, 24)
``` 
This Python function, sum_product, accepts a list of integers and outputs a tuple containing their sum and product. The function iterates through numbers in the list and accumulates their product and sum.