```python
def concatenate(strings: List[str]) -> str:
    return "".join(strings)

# Tests
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"

strings = []
result = concatenate(strings)
assert result == ""
```