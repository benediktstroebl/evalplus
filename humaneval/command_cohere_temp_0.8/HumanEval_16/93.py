Here's a Python script that contains a function to solve the problem you've outlined, along with a sample test to demonstrate its behavior:
```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of """
    return len(set(string.lower()))

# Test case
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

In this code, the `count_distinct_characters` function takes a string as its argument and returns the number of distinct characters within the string, regardless of case. It does this by converting the string to lowercase and then using a set, which automatically removes duplicate characters, giving a count of unique characters.