```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return result, product
# Example usage
numbers = [1, 2, 3, 4]
result_value, result_product = sum_product(numbers)
print("Result:", result_value)  
print("Product:", result_product)  
``` 
This code defines a `sum_product` function that calculates the sum and product of a list of integers. The function uses a list as a parameter, then iterates through each element in the list and updates the running sum and product variables accordingly. The final result is then a tuple containing the sum and product of the numbers in the list. 

Please note that this script is self-contained, meaning it does not require any additional imports or external functions to run successfully.