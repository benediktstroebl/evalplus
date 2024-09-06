```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple with sum and product of integers in the list.
    Args:
        numbers (List[int]): A list of integers
    Returns:
        Tuple[int, int]: A tuple with sum and product of the integers in the list
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
print(f"Sum: {result[0]}  Product: {result[1]}")  # Output: (10, 24)
```
This script defines a function sum_product that calculates the sum and product of a list of integers. It uses the standard loop to iterate over the list, updating the product and sum variables accordingly. The example provided uses this function to calculate the sum and product of the list [1, 2, 3, 4], and then prints the results, showing that the sum is 10 and the product is 24.