```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple containing sum and product of the list of integers.
    Args:
    numbers: List[int] 

    Returns: 
    Tuple[sum, product] 
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
print(result)  # Prints (6, 24)
``` 
The function **sum_product** is self-contained and takes a list of integers as input, then it calculates the sum and product of the numbers in the list, and returns a tuple containing both values. The test case provided is a simple list of integers and calls the **sum_product** function to calculate the sum and product of the numbers, and then prints the result.