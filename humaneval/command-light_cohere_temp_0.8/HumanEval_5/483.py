```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers+[delimeter] + numbers[1:] + [delimeter] + numbers[2:]

def test_intersperse():
    numbers = [1, 2, 3]
    delimiters = [4, 4, 4]
    result = intersperse(numbers, delimiters)
    assert list(result) == [1, 4, 2, 4, 3]

if __name__ == "__main__":
    test_intersperse()
```
This script defines a function `intersperse` that inserts a number `delimiter` between every two consecutive elements of an input list `numbers`. It also has a function `test_intersperse` which creates a test list and checks if the `intersperse` function outputs the correct result for the given input and delimiter.