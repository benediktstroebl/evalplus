Here's the solution:
```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 'ccc'

strings = ["abc", "a", "bb"]
print(longest(strings))  # Output: 'bb'

strings = []
strings. strings longest(["abc", "123", "a"])  # Output: 'abc'
```
This function takes a list of strings as input and returns the longest string in the list. If the list is empty, the function returns None. If there's a strings of the same length, it will return the first string encountered.