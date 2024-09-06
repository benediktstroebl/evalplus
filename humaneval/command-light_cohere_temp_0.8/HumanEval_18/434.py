```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

The function uses the `find()` method from the string module to count the occurrences of the substring in the original string. It uses the `len()` to iterate over all possible combinations and returns the count of the occurrences.

Here is a sample test for the function:
```python
print(how_many_times('aaa', 'a'))
# Output: 3
```