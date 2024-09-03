```python
def words_string(s):
    """
    Splits the string into words and returns an array of the words.
    """
    words can be separated by commas, spaces, or a mix of both.
    """
    example:
    'Hi, my name is John' 
    -> ['Hi', , 'my', 'name', 'is', 'John']
    'One, two, three, four, five, six' 
    -> ['One', 'two', 'three', 'four', 'five', 'six']
    """
    words = s.split(' ')
    words 
    return words

# Test cases
string1 = "Hi, my name is John"
string2 = "one two three four five six"
string3 = "hello world"

print(words_string(string1))  # Output: ['Hi', 'my', 'name', 'is', 'John']
print(words_string(string2))  # Output: ['one', 'two', 'three', 'four', 'five', 'six']
print(words_string(string3))  # Output: ['hello', 'world']
```