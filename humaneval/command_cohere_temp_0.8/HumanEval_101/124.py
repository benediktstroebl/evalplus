Here's a Python script that contains a function called `words_string` which takes a string as an input and returns a list of words from that string:
```python
def words_string(s):
    return s.split(', ')
```

The `words_string` function uses the `split` method to split the input string `s` using the `, ` as the separator. This method returns a list of strings, which are the words separated by the commas and spaces.

For example, given the input string "Hi, my name is John" the function returns the list ["Hi", "my", "name", "is", "John"].

This solution is straightforward and achieves the goal of splitting the string into words in a simple and efficient manner.