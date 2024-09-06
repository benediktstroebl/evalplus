```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test cases
string1 = 'xyzXYZ'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

string3 = 'abc123'
assert count_distinct_characters(string3) == 6

string4 = 'jABC123'
assert count_distinct_characters(string4) == 3
```  This function is designed to accept a string and return the number of distinct characters in that string, regardless of case. Using the `set` function, it achieves this by converting the string to lowercase and then using the `set()` function to create a set of all characters in the string. Finally, the length of the set is returned as the number of distinct characters.