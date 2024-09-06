```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, regardless of case.
    return:
    length of string str.
    """
lower case of each character in the string
    -1)
    """
    seen = set()
    count = 0
    for c in string:
        if c not in seen:
            seen.add(c)
            count += 1
    return count
```