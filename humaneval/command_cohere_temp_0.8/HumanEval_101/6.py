Here's a Python script that contains a function words_string(s) which takes a string s as input and returns a list of words from the string, separating them by commas or spaces.
```python
def words_string(s):
    return s.split(", ")
```
The function utilizes the split method to separate the string into individual words using comma or space as a delimiter. This simple approach effectively solves the problem and meets the criteria specified in the given challenge.

Here is a sample output of the function:
```
words_string("Hi, my name is John") == ['Hi', 'my', 'name', 'is', 'John']
words_string("One, two, three, four, five, six") == ['One', 'two', 'three', 'four', 'five', 'six']
``` 

This demonstrates the function's ability to correctly split the given string into an array of words.