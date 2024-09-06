```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c not in string. repeat()})

# Test cases
string = "xyzXYZ"
print(count_distinct_characters(string))  # Output: 3

string = "jerry"
print(count_distinct_characters(string))  # Output: 4
```
The solution uses a set to store characters, and then checks if each character exists in the set to count its distinctness. This approach works for any and handles all cases, including different letter cases, without needing to know the total number of characters in the input string.