```python
def strlen(string: str) -> int:
    """ Returns the length of a string """
    return len(string)
```
This function uses the built-in Python `len()` method to calculate the number of characters in the input string, which is the unambiguous definition of length for strings in Python. 

The function would be placed in a larger script that defines the tests, and the tests themselves could be written as:
```python
>>> strlen('')
0
>>> strlen('abc')
3
```
The first test checks the length of an empty string, and the second test checks the length of a three-character string. 
If you wanted to include this in a markdown code block, it would look like this:
```python
def strlen(string: str) -> int:
    """ Returns the length of a string """
    return len(string)

```
This would be the entire code block, and it can be run as-is to see the tests pass. Fixtures could be added to the top of the file to import into a larger test file if needed as well.