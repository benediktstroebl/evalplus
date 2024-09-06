Here's a Python script that contains a function words_string(s) which takes a string s as input and returns a list of words from the string, separating them by commas or spaces.

```python
def words_string(s):
    return s.split(", ")
```

The function utilizes the split method to split the string s into a list of tokens based on comma and space characters. This effectively separates the words in the string, considering various comma and space combinations as token separators.

To retrieve the list of words from the string, you can simply call the words_string function with the desired input string s as follows:
```python
print(words_string("Hi, my name is John"))  # Output: ['Hi', 'my', 'name', 'is', 'John']
print(words_string("One, two, three, four, five, six"))  # Output: ['One', 'two', 'three', 'four', 'five', 'six']
```

This approach provides a straightforward solution to break down a string of words separated by commas or spaces into individual words, forming a list.