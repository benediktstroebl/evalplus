```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates sum and product of integers in a list.
    if not numbers:  # Empty list
        return (0, 1) 
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test the function with a sample list
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24
``` 
The provided Python script defines a function called sum_product, which takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function first checks if the list is empty and returns a tuple of 0 and 1 if so. Otherwise, it initializes a product to 1 and a sum to 0, then iterates through the list, updating the product and sum. Finally, it returns the sum and product.