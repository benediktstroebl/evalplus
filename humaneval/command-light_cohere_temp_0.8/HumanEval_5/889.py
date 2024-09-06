```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + j for i, j in zip(numbers, numbers[1:])] + numbers

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 0, 0]
result = intersperse(numbers, delimiters)
shouldBe = [1, 2, 3, 4, 5]

# Print the results and compare
print("Test passed:", end)
print("Result:", end, sep=''")
for num, delimiter in zip(result, shouldBe):
    print(num, delimiter)
```