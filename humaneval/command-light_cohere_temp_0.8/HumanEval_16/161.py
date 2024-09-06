Here's a self-contained Python function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test cases
string1 = "xyzXYZ"
assert count_distinct_characters(string1) == 3

string2 = "jerry"
assert count_distinct_characters(string2) == 4

string3 = "abc123"
assert count_distinct_characters(string3) == 5 

# main input
string4 = input("hello")
assert count_distinct_characters(string4) == 8 

# expected output
```