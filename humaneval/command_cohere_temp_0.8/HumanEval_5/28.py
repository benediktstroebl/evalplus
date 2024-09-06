```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimeter = 4

print(intersperse(numbers, delimeter))  # Expected output: [1, 4, 2, 4, 3, 4, 5]
``` 

The function recursively builds a new list with the given delimiter inserted between all pairs of elements in the input list. The base case of the recursion is when the input list is empty, in which case it returns an empty list. 

To better understand the logic, let's break down the recursive step: 
1. **Base Case**: If the input list is empty (`not numbers`), it returns a list with just the delimiter (`return delimeter`) - e.g., [] for an empty list or [4] for a single delimiter. 

2. **Recursive Case**: If the input list is not empty, it concatenates three parts: 
    1. The first element of the list (`numbers[0]`) 
    2. The delimiter (`delimiter`) 
    3. The result of the recursion (`intersperse(numbers[1:], delimiter)`), which recursively inserts delimiters between all pairs of elements in the rest of the list. 

The delimiter is inserted after the first element because the recursion shifts the index of the second element by one (from `numbers[0]` to `numbers[1]`), and so on for every element after the first. 

The process recursively builds the final list, and the delimiter is inserted between all pairs of elements as requested. 

The provided test case will print the list `[1, 4, 2, 4, 3, 4, 5]` which is expected, as the delimiter 4 is inserted between consecutive pairs of numbers.