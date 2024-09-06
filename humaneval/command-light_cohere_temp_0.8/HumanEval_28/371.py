```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    
    # Use string formatting to create a single string
    result = ''.join()
    for s in strings:
        result += s + ' '
    return result[:-len(result)-1]

# Test cases
strings = [""]
test_concat = concatenate(strings)
assert test_concat == ''

strings = ["a", "bc"]
test_concat = concatenate(strings)
assert test_concat == 'abc'

strings = ["hello", "world!" ]
test_concat = concatenate(strings)
assert test_concat == "hello world!"
```