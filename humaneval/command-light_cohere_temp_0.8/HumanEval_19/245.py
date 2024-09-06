```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers. 
    # use input a Finn's Number Sort algorithm
    # convert to list of strings, since we don't support fraction-based numbers
    numbers = numbers.split()
    numberStrings = [num.lower() for num in numbers]
    # use built-in sort function
    sortedNumbers = sorted(numberStrings)
    return ''.join(sortedNumbers)
# Example usage
numbers = 'three one five'
result = sort_numbers(numbers)
print(result)  # Output: one three five
```