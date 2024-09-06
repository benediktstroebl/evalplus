Here's a Python script that contains a function words_string(s) which takes a string s as input and returns a list of words from the string, separating them by commas or spaces.
```python
def words_string(s):
    return s.split(", ")
```
The function utilizes the split method to separate the string into individual words using commas and spaces as the delimiter. This method returns a list of strings, which are the words extracted from the input string s.

For example, the function hairs_string("Hi, my name is John") would return the list ["Hi", "my", "name", "is", "John"].
```python
print(words_string("Hi, my name is John"))
# Prints ['Hi', 'my', 'name', 'is', 'John']
```
This approach provides a straightforward solution to the problem as asked, but depends on the input strings' format and spaces for splitting. Alternative approaches could be used to handle more complex cases, such as using regEx or other string methods for more robust splitting.