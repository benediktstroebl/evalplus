```python
def longest(strings: List[str]) -> Optional[str]:
    # Initialize the variable and return the longest string
    longest_str = strings[0] if strings else None
    return longest_str

# Test cases
strings = ["a", "bb", "ccc", "xx", "a"]
assert longest(strings) == "ccc"

strings = ["a"]
assert longest(strings) == "a"

strings = []
assert not_longest := longest(strings) is None
```