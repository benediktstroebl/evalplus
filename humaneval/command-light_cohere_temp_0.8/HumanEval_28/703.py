Certainly! Here's a self-contained Python function that solves the problem of joining strings in a list into a single string: 
```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
```
This function takes a list of strings as an argument and returns a string that is the concatenation of all the strings in the list.

This function is self-contained because it does not import any other modules or functions. It uses the string.slist only way strings and list comprehension to create a new string by joining all the strings together.

For example, if you have a list of strings like ['a', 'b', 'c'], you can use this function to get the concatenated string 'abc'.