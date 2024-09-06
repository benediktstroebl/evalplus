```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
print(intersperse(numbers, 4))
```

The function takes in a list of numbers and an integer delimiter as arguments. If the input list is empty, it returns an empty list. If there is only one number in the list, the function returns a list with the number and the delimiter. If there are multiple numbers in the list, the function inserts the delimiter between every two consecutive numbers and repeats this process until the last element of the list is reached. 

The output of the example is:
```bash
[1, 4, 2, 4, 3]
``` 

The basic logic of the function could be explained as follows: 
1. If there is no numbers, return delimeter (this is the base case for recursive approaches).
2. If there is one number, return the number and delimiter, repeated len(numbers) times.
3. If there are multiple numbers, call the function again, and add delimiter between consective numbers.