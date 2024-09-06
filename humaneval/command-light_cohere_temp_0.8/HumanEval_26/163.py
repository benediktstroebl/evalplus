```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [num]

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    print(remove_duplicates(numbers))
    print(expected)
    print(set(remove_duplicates(numbers)))
    print()
```
The function `remove_duplicates` takes a list of integers as input and returns a new list with unique integer occurrences. The function uses a set data structure to keep track of the seen integers, and it adds integers to the set once they are not present in the input list. The function then creates a new list and appends the integers that are not in the set.