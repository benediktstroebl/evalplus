Here's a Python script that contains a function called `words_string` which takes a string as an input and returns a list of words separated by commas or spaces:
```python
def words_string(s):
    return s.split()
```

The `words_string` function uses the `split()` method to split the input string s into a list of strings, using either commas or spaces as the delimiter. This method returns a list of the words in the string, separated by spaces, and without any punctuation or capitalization. Thus, the output of this function will be an array of words.

This approach assumes that the input string contains only words separated by spaces or commas, and doesn't account for other potential separators or more complex text cleaning requirements. 

For example, the test cases `words_string("Hi, my name is John")` and `words_string("One, two, three, four, five, six")` will both return `["Hi", "my", "name", "is", "John"]` and `["One", "two", "three", "four", "five", "six"]` respectively. 

It's important to note that this solution is straightforward and simple, and it may be suitable for basic cases. However, if you're dealing with more complex text-cleaning requirements, you may need a more sophisticated approach or additional preprocessing steps.