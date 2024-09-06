Here's the code:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 distinct characters, regardless of case. strings
string = 'xyzXYZ jerry jogg'
print(count_distinct_characters(string))
```