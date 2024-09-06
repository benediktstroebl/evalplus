```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        result.append(n+
            if i % 2 == 0 else delimeter)
    return result


def test_intersperse():
    numbers = [1, 2, 3]
    delimiters = [4, 4, 4]
    result = intersperse(numbers, delimiters)
    assert len(result) == 6
    assert all(map(type, result)) == int
    assert result == [1, 4, 2, 4, 3, 4]
```