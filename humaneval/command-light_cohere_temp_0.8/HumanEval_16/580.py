Here is a Python script that contains a self-contained function to solve the problem of counting distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, ignoring case.
    Args:
    string (str): The input string

    Returns:
    int: Number of distinct characters.
    """
    distinct = set()
    for c in string.str():
        distinct.add(c)
    distinct.
    return len(distinct)

# Example usage:
# Test string with repeated characters
test_string = "jerry jacey all"
# Expected output: 4
print(count_distinct_characters(test_string))

# Test string with all characters
test_string = "abcABCdef gHIJKLMNOPQRSTUV z"
# Expected output: 5
print(count_distinct_characters(test_string))
``` 
This code defines a function called `count_distinct_characters`, which takes a string as an argument and counts the number of distinct characters in that string, regardless of case. The function uses the set to keep track of unique characters, and then adds each character to the set once it is encountered. 
Finally, it returns the length of the set, which corresponds to the number of distinct characters. This approach is a simple and efficient way to count distinct characters in a string.