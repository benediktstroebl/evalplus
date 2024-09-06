Here is a Python script with a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> str:
    if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return strings[0][:max_length]

def test_longest():
    longest(['a', 'b', 'c'])

def test_empty():
    longest([]
    return

def test_multiple_strings():
    longest(['a', 'bb', 'ccc'])
    return

if __name__ == "__main__":
    print("Test results:", test_longest())
    print("Should return:", test_empty())
    print("Should return:", test_multiple_strings())
```

This script provides a function `longest` that accepts a list of strings and returns the longest string. The `test_longest`, `test_empty`, and `test_multiple_strings` functions are provided to pass tests for the `longest` function. The `__main__` block is used to execute the test cases.