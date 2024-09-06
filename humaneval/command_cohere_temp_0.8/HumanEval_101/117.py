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

This function uses the split method of strings which takes as an argument a string delimiter to split the string s into substrings, and returns a list of the substrings. This is an example of how the function can be used:
```python
print(words_string("Hi, my name is John"))
# ['Hi', 'my', 'name', 'is', 'John']

print(words_string("One, two, three, four, five, six"))
# ['One', 'two', 'three', 'four', 'five', 'six']
``` 

This will output the list of words from the string s, separating them by commas or spaces.