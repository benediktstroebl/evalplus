Here's a self-contained Python function that computes the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

#Test cases
assertEqual(strlen(''),       0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('123 abc')) 5
assertEqual(strlen('   ')), 5
# Larger strings
assertEqual(strlen('hello world')), 13
assertEqual(strlen('ABCDEFGHIJKLMNOPQRSTUV')) 21
```
This code defines a function `strlen` that calculates the length of a given string. It takes an input argument of type `str` which is expected to be a string. The function then returns an length of this string as an integer. 

Please note that you can use this function in your markdown code block, and it will provide the output as expected.