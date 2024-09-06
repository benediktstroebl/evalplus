Here's the solution to the Markdown code block problem using Python:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    if not numbers:  # Empty list
        return (0, 1)
    return (sum(numbers), product(numbers))
    product(numbers) = sum(map(int, numbers)))
    return (sum(numbers), product(numbers))

# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)
result = sum_product([].integers())  # [].integers() is an error
``` 
Another solution to the problem is to create an iterative function that calculates the sum and product using a generator expression.