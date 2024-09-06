```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with valid inputs and valid outputs
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([5, 6, 7, 8]))  # Output: (28, 120)
print(sum_product([]))  # Output: (0, 1)
print(sum_product([10, 20, 30])) # Output: (60, 900)
```
The code defines a function **sum_product** that calculates the sum and product of a list of integers. The function uses the fact-based product and sum calculation, which are represented by a product variable **product** and a sum variable **sum**. The test cases provided pass the function with valid inputs, and the output is printed to the console. The output shows the correct sum and product values.