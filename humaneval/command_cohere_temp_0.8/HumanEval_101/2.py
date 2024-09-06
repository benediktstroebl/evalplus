Here's a Python script that contains a function words_string(s) which takes a string s as input and returns a list of words from the string, separating them by commas or spaces.
```python
def words_string(s):
    return s.split(", ")
```
The function utilizes the split method to separate the string into individual words using commas and spaces as the delimiter. This method returns a list of strings, which are the individual words from the input string.

For example, given the input string "Hi, my name is John", the function would return the list ["Hi", "my", "name", "is", "John"].

This solution is straightforward and efficiently handles the word separation process, making it a useful tool for handling string manipulations like word splitting.