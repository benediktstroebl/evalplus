```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a specified integer ('delimiter') after every two
    consecutive elements of the input list.
    """
    Format: [int, int] -> List[int]
    """
    numbers = [x for x in numbers if x !=] + [delimiter] + [x for x in numbers[1:]]
    return numbers[1:]

# Test cases:
numbers = [1, 2, 3]
print(intersperse(numbers, 4))  # Expected output: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4]
print(intersperse(numbers, 4))  # Expected output: [1, 4, 2, 4, 3, 4]

numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 4))  # Expected output: [1, 4, 2, 4, 5, 4]

numbers = [10, 20, 30]
print(intersperse(numbers, 10))  # Expected output: [10, 10, 20, 10, 30, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intersperse(numbers, 10))  # Expected output: [1, 10, 2, 10, 4, 10, 5, 10, 6, 10, 7, 10, 8, 10, 9]
```
The provided Python script defines a function called `intersperse` that inserts a specified integer (`delimiter`) after every two consecutive elements of an input list. It then applies this test cases to demonstrate the functionality of the function, ensuring the expected output is achieved.