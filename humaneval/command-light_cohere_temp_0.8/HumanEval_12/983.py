```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return strings[0][:max_length]

# Test case
strings = ["a", "bb", "ccc"]
result = longest(strings)
assert isinstance(result, str) and len(result) == 3, "Error"

# Test case with empty list
strings = []
result = longest(strings)
assert result is None, "Error"

# Test case with non-string input
numbers = [1, 2, 3, 4, 5]
result = longest(numbers)
assert isinstance(result, NoneType), "Error"

# Test case with list of different lengths
strings = ["a", "b", "c"]
result = longest(strings)
assert isinstance(result, str) and len(result) == 2, "Error"
```
This Python script defines a function called `longest`, which takes a list of strings as input and returns the longest string found in the list. It then tests this test the both the expected output and the function's behavior with various test cases.