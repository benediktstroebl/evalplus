```python
def count_distinct_characters(string):
    return len(set(string.lower()))

x = 'xyzXYZ'
y = 'jerry'

# Test case 1
print(count_distinct_characters(x))  # Output: 3

# Testcase 2
print(count_distinct_characters(y))  # Output: 4
```
This function calculates the number of distinct characters in a given string, regardless of case. The set function is used to create an unordered collection of characters from the input string, and the len function is used to count the number of elements in the set. The function returns the result.