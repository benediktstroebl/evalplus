```python
def count_distinct_characters(string):
    """
    Count distinct characters in a given string, ignoring case.
    return: number of distinct characters
    """
    import re
    char_count = len(re.findall(r'\w+/', string.findall(r'\w+', string))
    return char_count

# Test the function
string1 = 'xyzXYZ'
result1 = count_distinct_characters(string1)
print("First string result:", result1)

string2 = 'jerry'
result2 = count_distinct_characters(string2)
print("Second string result:", result2)

string3 = 'hello'
result3 = count_distinct_characters(string3)
print("Third string result:", result3)
```
The function `count_distinct_characters` takes a string as input and returns the number of distinct characters in the string, regardless of case. Using the `findall` function and `re.php.replaceall`, theSpin willed the important data and matches the regular expression 'w+/', which matches one or more whitespace characters.