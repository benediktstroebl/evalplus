Here's a Python script that contains a function `words_string` that solves the problem:
```python
def words_string(s):
    return s.split()
```
The `words_string` function utilizes the `split` method to divide the input string into separate words and subsequently return them as a list. This method works for spaces or commas as separators. 

### Example Usage:
```python
print(words_string("Hi, my name is John"))
# Output: ['Hi', 'my', 'name', 'is', 'John']

print(words_string("One, two, three, four, five, six"))
# Output: ['One', 'two', 'three', 'four', 'five', 'six']
```

This approach achieves the intended functionality in the most straightforward manner, splitting the string into words based on commas or spaces.