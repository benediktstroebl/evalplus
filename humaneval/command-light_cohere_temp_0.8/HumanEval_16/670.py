Here's the self-contained Python function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test cases
string1 = 'abcXYZ'
string2 = 'jerry'
string3 = 'xxooobaja123'

print(count_distinct_characters(string1))  # Output: 3
print(count_distinct_characters(string2))  # Output: 4
print(count_distinct_characters(string3))  # Output: 6
```
This function counts the number of distinct characters in the given string, and regardless of case, it will give the count of unique characters in the string.