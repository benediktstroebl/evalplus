```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]) + delimeter
        else:
            result.append(numbers[i])
    return result

def test_ints_intersperse():
    numbers = [1, 2,3,4,5]
    delimiters = [0, 4, 0, 4, 0]
    expected = [1, 4, 2, 4, 3, 5]
    return expected == intersperse(numbers, delimiters)
```