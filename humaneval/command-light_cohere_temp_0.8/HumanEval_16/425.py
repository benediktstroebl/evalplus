```python
def count_distinct_characters(string):
    return len([c for c in string. characters() if c.isalpha()])
 if isinstance(string, str) else "Input must be a string"

#Test cases
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('ABC') == 3
assert count_distinct_characters('XyX') == 3
assert count_distinct_characters('JERRY') == 4
assert count_distinct_characters('') == 0
```