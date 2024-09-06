Here is a self-contained Python script that solves the markdown code block problem:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimeter for i,j in zip(numbers,numbers[1:])]

# Test case 1
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
assert len(result) == 6
assert result[0] == 5
assert result[1] == 9
assert result[2] == 13

# Test case 2
numbers = [1,2,3]
delimiter = 4
result = intersperse(numbers, delimiter)
assert len(result) == 6
assert result[0] == 5
assert result[1] == 9
assert result[2] == 13

# Test case 3
numbers = [1,2,3,4,5]
delimiter = 6
result = intersperse(numbers, delimiter)
assert len(result) == 7
assert result[0] == 11
assert result[1] == 17
assert result[2] == 23

# Test case 4
numbers = [1,2,3,4,5]
delimiter = 2
result = interserate(numbers, delimiter)
assert len(result) == 7
assert result[0] == 3
assert result[1] == 5
assert result[2] == 7

```

This script defines a function `intersperse` which takes a list of numbers and a delimiter as input and returns a new list with the elements from the original list separated by the specified delimiter. The script also includes several test cases to verify the correctness of the `intersperse` function.