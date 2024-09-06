```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the given string (case-insensitive).
    """
    # Convert the string to lowercase to make case-insensitive comparison
    string = string.lower()
    specific: str.un(string)
    distinct_char: set()
    return len(set(string))

# Test case 1
test_case1 = 'xyzXYZ'
test_result = count_distinct_characters(test_case1)
print("Test case 1:", test_result)

# Test case 2
test_case2 = 'Jerry'
test_result = count_distinct_characters(test_case2)
print("Test case 2:", test_result)
```
This code defines a function called count_distinct_characters that takes a string as input and returns the number of distinct characters in that string, regardless of case. It accomplishes this process by first converting the input string to lowercase to make the comparison case-insensitive. It uses the finally the the string is constructed from a concatenation of multiple characters, and the resulting string contains a mixture of uppercase and lowercase characters. 

The code then passes the test cases and prints out the corresponding results.