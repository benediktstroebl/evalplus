```python
def concatenate(strings: List[str]) -> str:
    return "".join("".join(strings))

print(concatenate([]))      # Output: empty string ''
print(concatenate(['a']))   # Output: 'a'
print(concatenate(['a', 'b']))  # Output: 'ab'
print(concatenate(['a', 'b', 'c'])) # Output: 'abc'
```
This Python function concatenate accepts a list of strings and returns the concatenated result as a single string. The output of the test cases are provided to verify the expected output of the function.

The output of this function for the given input will be the string "abc".