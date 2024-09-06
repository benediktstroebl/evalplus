Here's a Python script that contains a function `words_string` that solves the problem:
```python
def words_string(s):
    return s.split()
```
The task is to split the string into words and return an array of the words. The `split()` method in Python splits the string using a specified delimiter or whitespace (including commas and spaces) into a list. The split() method also accepts optional parameters to control the splitting behavior, such as maximum splits and custom delimiters, but the default behavior works for this particular problem. This method conveniently accomplishes the task without requiring a loop to manually split the string, making it efficient and straightforward.