```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a given string, regardless of case.
    return: 
    ASCII values vary from 0 to 127.
    Let's also count all uppercase, lowercase and non-alphabetic characters
    """
    char_set = set(string)
    return len(char_set)

# Test the function
string1 = "xyzXYZ"
result1 = count_distinct_characters(string1)
print("First string result:", result1)

string2 = "jerry"
result2 = count_distinct_characters(string2)
print("Second string result:", result2)

# Test with non-alphabetic characters
string3 = "123"
result3 = count_distinct_characters(string3)
print("Third string result:", result3)
```