```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, ignoring case.
    Return an integer count of distinct characters.
    """
    string = 'xyzXYZ'
    return len(set(string))

# Test case 1
string = 'jerry'
result = count_distinct_characters(string)
print(result)

# Testcase 2
string = 'jerry Johnson'
result = count_distinct_characters(string)
print(result)

# Testcase 3
string = 'JERRY'
result = count_distinct_characters(string)
print(result)
```