```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:])+[delimeter]]

# Test the function with a sample input and expected output
numbers = [1, 2, 3]
delimiters = [0, 4]

result = intersperse(numbers, delimiters)
assert len(result)==len(numbers) # check if the length is the same
assert list(map(lambda x:x==numbers[0],result)) == True # check if each element of the output list is the same as the corresponding element in input list
print(result)
```