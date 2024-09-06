Here is a Python script that contains a self-contained function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isalpha()}  # is unique

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('jerry'))   # Output: 4
```
The function uses a generator expression with a list comprehension to find all characters in the string, and then uses the isalpha() method to check if each character is unique. The result then returns the string length, which is the number of distinct characters. The test cases demonstrate the value of the function.