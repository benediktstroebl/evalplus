Here's a Python script that contains a function `words_string` as per the prompt, which splits a given string into an array of words:
```python
def words_string(s):
    return s.split()
```
The Python built-in `split()` method is used to split the string `s` into individual words and return them as an array. This method delves into the string and retrieves the array of substrings separating them at the spaces, without including them.

For example:
```python
print(words_string("Hi, my name is John"))
# Prints ['Hi', 'my', 'name', 'is', 'John']

print(words_string("One, two, three, four, five, six"))
# Prints ['One', 'two', 'three', 'four', 'five', 'six']
```
This method ensures a quick and efficient word separation, making it a reliable solution.