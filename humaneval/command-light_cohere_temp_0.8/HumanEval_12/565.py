```python
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len)

# Test cases
strings = ["a", "b", "c"]
assert longest(strings) == "c"

strings = ["a", "bb", "ccc"]
assert longest(strings) == "ccc"

strings = []
assert nother = longest(strings) == None

strings = ["python", "javascript", "algorithm"]
assert longest(["python", "javascript", "algorithm"]) == "javascript"
```
The function `longest` takes a list of strings and returns the longest string in the list. The `max` function is used with the `key` argument set to `len`, so that the function returns the length of the longest string.