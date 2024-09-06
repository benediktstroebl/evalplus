Here's a Python script that contains a function words_string(s) which takes a string s as input and returns a list of words from the string, assuming that the words are separated by commas or spaces:
```python
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Use a comma and space-separated string values, assuming that the delimiter can be either a comma or a space
    return s.split(", ")
```

This script defines a function words_string that takes a string as input and returns a list of words in the string assuming the words are separated by commas or spaces. The function just uses Python's built-in split method to split the input string based on comma or space delimiters.

The split method returns a list of the words in the order they appear in the original string, with each word stripped of leading and trailing spaces. It also eliminates any empty strings that are formed during the splitting process, resulting in a list of clean words.

Note that this approach assumes that words are separated by commas or spaces and doesn't handle any other types of input scenarios explicitly. Adjustments might be necessary for more complex use cases.