```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, regardless of case.
    """
    return len(set(string.lower()))
```

Here's a detailed breakdown of the code:
 - A function named `count_distinct_characters` is defined, taking a single parameter `string: str`. This parameter represents the input text.
 - Inside the string is converted to lowercase using `string.lower()` to ensure case of character comparisons. This way converts all text into a case-insensitive form, which is needed to count distinct characters.
 - The `len()` function is used to return the length of the set of lowercase characters in the string, which effectively counts the number of distinct characters.
 - This output is the return value of the `len()` function, which represents the count of distinct characters.

This code is a complete, self-contained solution to the problem of counting distinct characters in a given string, regardless of case. It can be easily to pass tests and is a good example of writing Python functions with descriptive and clear code.