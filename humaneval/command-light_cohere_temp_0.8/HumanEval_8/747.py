```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Testing the function
test_list = [1, 2, 3, 4]
result = sum_product(test_list)
print("Sum:", result)
print("Product:", result[1])
test_list = []
result = sum_product(test_list)
print("Sum:", result)
print("Product:", result[1])
``` 
This code defines a `sum_product` function that calculates the sum and product of a list of integers. The function uses a loop to iterate over the list, multiplying each number with the product and adding them to the sum. The product is then set to 1, and the function returns a tuple containing the sum and product. 

It then tests the function by passing an empty list, and also a list of integers, and it prints the results of the product calculation.