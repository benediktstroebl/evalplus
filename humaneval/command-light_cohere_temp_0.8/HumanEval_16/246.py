Here's a self-contained Python script that defines a function `count_distinct_characters` solving the problem you described:

```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in the given string, regardless of case.
    string = string.lower()
    common = set() = set()
    count = 0
    for c in string:
        if c not in common:
            common.add(c)
            count += 1
    return count
```