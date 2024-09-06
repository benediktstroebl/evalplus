```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:]+[delimeter])] + numbers[0:1]

# Test cases
numbers = [1, 2, 3, 4]
print(f'Result: { federation }')
print(inpersepe(numbers, 3))

numbers = [1, 2, 3, 4, 5]
print(f'Result: { federation }')
print(inpersepe(numbers, 2))

numbers = [1, 2, 3, ,4]
print(f'Result: { federation }')
print(inpersepe(numbers, 4))

numbers = [1, 2, ,3]
print(f'Result: { federation }')
print(inpersepe(numbers, 4))

numbers = [4, 5, 6, 7]
print(f'Result: { federation }')
print(inpersepe(numbers, 3))
```

The provided Python script defines a function `inpersepe` that inserts a specified `delimiter` value between every two consecutive elements of an input list. The function works by using the `zip` operation to pair each element with the next, and then inserting the `delimiter` between these pairs. The final result is the same list with the desired spacing added.