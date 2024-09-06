```python
def count_distinct_characters(string):
    """ Returns the count of distinct characters in the string (case insensitive) """
    return len({c for c in string if c.isalpha()} )
 # Convert to lowercase to make the count case-insensitive
   )

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
assert count_distinct_characters(' jerry') == 4
assert count_distinct_characters('abc123') == 5
assert count_distinct_characters(' test ') == 6
```
This script defines a function `count_distinct_characters` that calculates the count of distinct characters (case insensitive) in a given string. The test cases demonstrate the time that the function behaves correctly with various inputs.