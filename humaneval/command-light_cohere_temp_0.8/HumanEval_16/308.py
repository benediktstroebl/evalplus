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
This code defines a function **count_distinct_characters**, which accepts a string and returns the count of distinct characters in it, regardless of case. This function employs the _ set() function with the string's lowercase version to obtain the distinct characters, and then uses the len() function to calculate the count.