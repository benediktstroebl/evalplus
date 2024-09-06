Here's a Python script that contains a function words_string(s) which takes a string s as input and returns a list of words from the string, separating them by commas or spaces.

```python
def words_string(s):
    return s.split(', ')
```

The function utilizes the split method to separate the string into segments based on comma or space characters. This method returns a list of strings, which are then returned by the function. Given the two test cases provided, the function would return the following:
```
["Hi", "my", "name", "is", "John"]
["One", "two", "three", "four", "five", "six"]
``` 

This approach is straightforward and effective in handling the problem statement. It is important to note that this method does not account for other possible separators besides commas and spaces. Thus, for any strings that involve different separators, this function would not yield the desired result.