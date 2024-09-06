```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function
test_list = [1, 2, 3, 4, 5]
result = sum_product(test_list)
print("Sum:", result)
print("Product:", result[1])

test_empty = []
result_empty = sum_product(test_empty)
print("Empty Sum:", result_empty)
print("Empty Product:", result_empty[1])

test_single = [5]
result_single = sum_product(test_single)
print("Single Number Sum:", result_single)
print("Single Number Product:", result_single[1])
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function is then tested with various scenarios, including empty lists, single numbers, and lists of numbers. The output displays the results for each test case.