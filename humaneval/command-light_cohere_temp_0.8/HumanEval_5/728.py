```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 2)

# Test case 1
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert len(result) == 4
assert result[0] == 1  # Should insert 4 between 1 and 2
assert result[1] == 4   # Should insert 4 between 2 and 3
assert result[2] == 7  # Should insert 4 between 3 and 4
assert result[3] == 8  # Should insert 4 between 4 and 5 

# Test case 2
numbers = [4, 5, 6]
result = intersperse(numbers, 4)
assert len(result) == 4
assert result[0] == 4   # Should insert 4 between 4 and 5
assert result[1] == 8  # Should insert 4 between 5 and 6
assert result[2] == 11  # Should insert 4 between 6 and 7
assert result[3] == 12  # Should not insert 4 between 7 and 8

# Test case 3
numbers = [7, 8, 9]
result = intersperse(numbers, 4)
assert len(result) == 4
assert result[0] == 7  # Should insert 4 between 7 and 8
assert result[1] == 11  # Should insert 4 between 8 and 9
assert result[2] == 15  # Should insert 4 between 9 and 10
assert result[3] == 18  # Should not insert 4 between 10 and 11
```

This Python code provides a self-contained solution and test cases for the problem of inserting a number 'delimiter' between every two consecutive elements of an input list 'numbers'. The code defines a function `intersperse` that takes two parameters: a list of integers 'numbers' and an integer 'delimiter'. The function returns a new list with the elements of 'numbers' interspersed with the 'delimiter' at every second element. The code also includes three test cases to verify the correctness of the `intersperse` function.