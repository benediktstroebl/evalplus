```python
def concatenate(strings: List[str]) -> str:
    return ''.join("".join(strings))

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result) # Output: abc

strings = []
result = concatenate(strings)
print(result) # Output: ''

strings = ["a", "b", "c"] + ["d"]
result = concatenate(strings)
print(result) # Output: adc

strings = ["aa", "bb", "cc"]
result = concatenate(strings)
print(result) # Output: aabbcc
```