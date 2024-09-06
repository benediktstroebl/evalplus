```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in the list.
    Args:
        numbers: A list of integers

    Returns:
        A tuple consisting of a sum and a product of all the integers in the list.
    """
    sum = 0
        product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

``` 
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function iterates through the integers in the list, updating the running sum and product accordingly. It returns a sum and product as a tuple. 
Finally, the code tests the `sum_product` function with sample inputs and prints the results.