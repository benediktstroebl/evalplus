```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.count(character)
    return len(characters)

# Tests
string1 = "xyzXYZ"
assert count_distinct_characters(string1) == 3

string2 = "jerry"
assert count_distinct_characters(string2) == 4

string3 = "hello"
assert count_distinct_characters(string3) == 5
```