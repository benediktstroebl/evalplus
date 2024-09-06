```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers] + [num for num in numbers]

# Unit tests:
numbers = [1, 2, 3, 4, 5]
test_intsperse = [int(i) for i in '1234']

assertEqual(intsperse(numbers, 3), test_intsperse)
assertEqual(intsperse(test_intsperse, 4), [3, 12, 14])
```  This script defines a function `intsperse` that separates every two consecutive elements in the input list by adding a delimiter to the previous element.  and then resulting list with the final element.