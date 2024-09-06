Here's a Python script that contains a function `words_string` as per the prompt:
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

This function uses the `split` method on the string `s` with `', '` as the separator to return a list of words. The separators ', ' represent commas and spaces, allowing for flexibility in the input format.

To make this solution more robust, we could implement error handling to deal with unexpected separators or empty inputs, like so:
```python
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    if not s:
        return []
    return s.split(', ')
```

This version of the function returns an empty list if the input is empty. It does not assume any particular format for the input text, allowing it to gracefully handle a variety of inputs.