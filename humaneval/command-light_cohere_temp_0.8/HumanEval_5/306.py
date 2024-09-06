```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i, j in zip(numbers, numbers[1:])] + numbers

#Test cases
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
print(f'Test case 1 result: {expected})

numbers = [1, 2, 3]
delimiter = 7
expected = [1, 14, 12, 19]
print(f'Test case 2 result: {expected})

numbers = [1, 2, 3, 4]
delimiter = 4
expected = [1, 5, 9, 13]
print(f'Test case 3 result: {expected})
```
The provided Python script defines a function `inespereselect` that takes a list of integers and a delimiter as input and returns a new list with the elements of the original list separated by the provided delimiter. The `test_cases` section demonstrates the function's behavior by applying it to different lists of integers and printing the expected results.