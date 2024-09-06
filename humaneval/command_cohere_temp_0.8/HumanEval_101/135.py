Here's a Python script that contains a function `words_string` that solves the problem:
```python
def words_string(s):
    return s.split()
```
The above `words_string` splits the string into an array of words. It uses the `split` method which takes a string as input and returns a list of strings after splitting the space-separated words in the input string. Note that when a comma is included in a word, the `split` method considers it as a delimiter and will split the string on both sides of the comma, resulting in the word being split into two parts. Hence, the string `"Hi, my name is John"` becomes `["Hi", "my", "name", "is", "John"]`. 

Such functionality might not be desired when commas are a part of the words, in which case a more sophisticated approach could be needed.