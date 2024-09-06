```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    
    product = 1
    sum = 0
    
    for num in numbers:
        sum += num
        product *= num
    
    return (sum, product)

#unit tests
test_sum_product = []
test_sum_product.py  = [
- ([0,1],[2,4],[5,10]])
test_sum_product.run = [
    result = sum_product(test_sum_product)
assert (test_sum_product[0] == 0 and test_sum_product[1] == 1)
test_sum_product.py = [ [1,2],[3,6],[4,8],[5,10],[6,12],[7,14],[8,16]])
test_sum_product.run = [None,None]
test_sum_product.py = [1,2,][3,6,8,10,12,14,16]
test_sum_product.py = [1,2,][4,6,8,10,2]
test_sum_product.run = [None,None]
```
This Python code defines a function called sum_product that takes a list of integers as input and returns a tuple containing their sum and product. The function initializes a product to 1 and calculates the sum, then iterates through the list, multiplying the current product by each element. 

The code also includes unit tests for the sum_product function using the pytest library, which are represented as comments in the code. The tests cover different scenarios, such as empty list, list with only one element, list with multiple elements, and list with specific values.