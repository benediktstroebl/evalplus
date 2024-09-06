```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
#Test case 1
print(sum_product([1, 2, 3, 4]))  #Expected Output: (10, 24)
#Test case 2
print(sum_product([]))       #Expected Output: (0, 1)
#Test case 3
print(sum_product([5, 6, 7]))  #Expected Output: (15, 28)
``` 
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It utilizes a type hint of `List[int]` for the parameter `numbers` which allows the function to accept a list of integers as input. The function iterates through the each number in the list, adding them to the sum, and multiplying them to the product. This is output is a tuple consisting of the sum and product.