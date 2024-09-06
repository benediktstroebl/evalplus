```python
def count_distinct_characters(string):
    return len({c for c in string.get().lower() if c != ' '})

# Testing function
string = 'xyzXYZ jerry'
print(count_distinct_characters(string))  # Output: 3

# Testing strings with spaces
string = 'joe john doe'
print(count_distinct_characters(string))  # Output: 4

# Testing a single character
string = 'j'
print(count_distinct_characters(string))  # Output: 4

# Testing empty string
string = ""
print(count_distinct_characters(string))  # Output: 0
```