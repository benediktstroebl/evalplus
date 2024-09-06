```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()} )
   solely to lowercase or uppercase letters.

test_function = count_distinct_characters('abc ABC')
 assert test_function == 3

test_function = count_distinct_characters('XyX')
 assert test_function == 3

test_function = count_distinct_characters('jerry')
 assert test_function == 4
```