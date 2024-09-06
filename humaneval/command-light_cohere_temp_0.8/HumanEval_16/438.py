```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isalpha()})
 distinct characters, regardless of case.

# Test case 1: Single string with all uppercase characters
print(count_distinct_characters('XYZ'))     # Output: 3

# Test case 2: Single string with all lowercase characters
print(count_distinct_characters('jerry'))    # Output: 4

# Test case 3: Single string with a mix of uppercase and lowercase characters
print(count_distinct_characters('jerryZ'))    # Output: 3

# Test case 4: Empty string
print(count_distinct_characters(""))    # Output: 0
```
The above Python script defines a function **count_distinct_characters** that calculates the number of distinct characters in a given string. It uses a straightforward itertools.isalpha() technique to determine whether character as distinct if it's not equal to the current character, regardless of case. The test cases provided demonstrate the results.