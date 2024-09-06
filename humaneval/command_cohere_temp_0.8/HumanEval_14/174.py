```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The function constructs a list of prefixes of the given string and then returns the list excluding the last element (which would be the full string itself, prefixed with '%').

To do this it iterates over the length of the string and constructs prefixes of the string starting from the first character and ending with the full string. The '%' sign is appended after each prefix to distinguish between prefixes especially when the input string is a single character. 

The resulting list of prefixes is then returned excluding the last element which is the full string prefixed with '%'. 

The unit test included would test the function with different strings and assert if the result is as expected. 
```python
def test_all_prefixes():
    assert all_prefixes("abc") == ["a", "ab", "abc"]
    assert all_prefixes("hello") == ["h", "he", "hel", "hello"]
    assert all_prefixes("foo") == ["f", "fo", "foo"]
    assert all_prefixes("foo_bar") == ["f", "fo", "foo", "foo_", "foo_b", "foo_ba", "foo_bar"]
```