```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[0]]
    
if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    print(result)
```
This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with unique integer values. The function utilizes a set data structure to keep track of seen numbers, then iterates through the input list and adds numbers to `seen` only if they are not in the original list or if the current number is not in the list.

The `main` block contains the test code that creates a list of integers and passes it to the `remove_duplicates` function. The output of this list is then printed to the console.