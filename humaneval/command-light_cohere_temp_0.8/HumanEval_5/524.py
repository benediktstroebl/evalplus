```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        result.append(numbers[i] + delimeter if i < len(numbers) - 1 else numbers[i])
    return result
# Test cases are self-contained within the code block
# Test case 1
numbers = [1, 2, 3]
result1 = intersperse(numbers, 4)
print(result1)  # Expected output: [1, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3, 4]
result2 = intersperse(numbers, 5)
print(result2)  # Expected output: [1, 5, 2, 5, 3, 4]

# Test case 3
numbers = [1, 2, 3]
result3 = intersperse(numbers, 1)
print(result3)  # Expected output: [2, 1, 3]
```
This code defines a function `intersperse` that takes two parameters - a list of numbers and a delimiter as an integer. It then loops through the A list of numbers and adds the next number after the previous number if there's a next number. Otherwise, it adds the number to the current number in the list, effectively inserting the delimiter between every two numbers.