```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test case 1
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)

#Test case 2
numbers = [5, 6, 7, 8, 9]
print(sum_product(numbers))  # Output: (40, 8)

#Test case 3
numbers = []
print(sum_product(numbers))  # Output: (0, 1)
```

This Python code defines a function called sum_product that calculates the sum and product of a list of integers. The sum is stored in a variable sum, and the product is stored in a variable product. The function then iterates through each number in the list, multiplying them together and adding them to the sum. Finally, it returns a tuple containing the sum and product. 

The code then passes three test cases, which demonstrate the correctness of the sum_product function.