Here's a Python script that contains a function words_string(s) which takes a string s as input and returns a list of words from the string, separating them by commas or spaces.
```python
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return s.split(', ')
```

This function uses the split method of strings which takes as an argument a string delimiter to split the string s into substrings. It returns a list of the words of s split by commas or spaces, ready for use in your Python applications. Feel free to adapt this code for your specific needs and explore the multitude of possibilities in Python!