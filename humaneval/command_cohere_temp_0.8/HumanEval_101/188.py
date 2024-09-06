Here's a Python script that contains a function words_string(s) which takes a string s as input and returns a list of words from the string, separating them by commas or spaces.
```python
def words_string(s):
    return s.split()
```
The method used here is s.split(), which provides a list of the words in the string s, separated by spaces. Alternatively, we could have used s.split(','), which would separate the words by commas. In either case, the result is a list of the individual words from the input string.