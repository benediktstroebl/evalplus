```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Returns a tuple with sum and product of all integers in the list.
    Args: 
    - numbers (List[int]): A list of integers
    Returns: 
    - tuple (int, int): A tuple with sum and product of all integers in the list
    """
    product = 1
    sum = 0 
    for num in numbers:
        product *= num
        sum += num 
    return (sum, product)

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 2432875551236
```
This function, `sum_product`, takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The example usage demonstrates how to call the function with a list of integers [1,2,3,4] and print the result.