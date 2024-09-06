Here's a self-contained Python function that concatenates a list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Example usage:
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: 'abc'

# Test cases:
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
This function takes a list of strings as an argument and concatenates them into a single string, returning the result. 
The tests ensure the validity of the function's behavior.