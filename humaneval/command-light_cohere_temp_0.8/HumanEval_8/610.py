```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of integers in a list.
    Args:
        numbers (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing sum and product of all integers in numbers list
    """
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```