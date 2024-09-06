```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    :return numbers with separators
    """
    """
    return numbers[:-1:-1] + [delimeter] + numbers[-1:]

tests = [
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([10, 20, 30], 10) == [10, 20, 30]
    assert intersperse([10, 20], 10) == [10, 20]
    assert intersperse([1, 2, 3], 0) == [1, 2, 3]
    assert intersperse([], 0) == []
```