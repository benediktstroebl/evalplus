```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers) - 1):
        if i % 2 == 0:
            result.append(numbers[i]+delimiter)
        else:
            result.append(numbers[i])
    return result

# Test case 1: empty list
print(inperse([], 4))

# Test case 2: list with odd index
print(inperse([1, 2, 3], 4))

# Test case 3: list with even index
print(inperse([1, 2, 3, 4], 4))

# Test case 4: list with two consecutive elements
print(inperse([1, 2, 3], 4))

# Test case 5: list with three consecutive elements
print(inperse([1, 2, 3, 4], 4))
```
The function `inperse` uses a list comprehension and the `append` function to insert a delimiter between every two consecutive elements of the input list. The output of the `print()` is a list of lists, with the delimiters in between the elements.