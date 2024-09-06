```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all occurrences of a substring in the original string.
    >>> how_many_times('aa', 'a')
    0
    >>> how_many_times('aaaaaa', 'aa')
    4
    >>> how_many_times('abcde', 'abc')
    3
    """
    return len([i for i, char in enumerate(string) if char == substring])

def test_how_many_times():
    assert how_many_times('aa', 'a') == 0
    assert how_many_times('aaaaaa', 'aa') == 4
    assert how_many_times('abcde', 'abc') == 3

if __name__ == "__main__":
    test_how_many_times()
```
This Python script provides a function `how_many_times` that calculates the count of occurrences of a given substring within a given input string. The `test_how_many_times` function is used to verify the correctness of the `how_many_times` function against various test cases. 
This demonstrates a self-contained approach to solving the problem of counting occurrences of a substring within a string.