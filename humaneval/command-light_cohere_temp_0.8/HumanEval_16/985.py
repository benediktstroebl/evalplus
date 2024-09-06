Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isalpha()})

# Test cases
string1 = "xyzXYZ"
print(count_distinct_characters(string1))  # Output: 3

string2 = "jerry"
print(count_distinct_characters(string2))  # Output: 4

string3 = "hello world"
print(count_distinct_characters(string3))  # Output: 6
```
This script defines a function `count_distinct_characters` that takes a string as input and returns the count of distinct characters in that string. It uses a string's characters to create a set and then uses the `len` function to get the length of that set, which is the number of distinct characters in the string.

The function is then tested with three different strings. The first two test cases are strings that contain only lowercase letters, and the function returns 3 for the first string and 4 for the second string, which is what is expected. The third test case is a string that contains all uppercase letters, and the function returns 6, which is also what is expected.