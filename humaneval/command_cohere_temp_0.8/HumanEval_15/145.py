```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
```
The function 'string_sequence' takes an integer 'n' as input and returns a string consisting of space-separated numbers ranging from 0 to 'n' inclusive. 

To achieve this, it uses the 'range' function to generate a sequence of numbers from 0 to 'n' and then applies the 'map' function to convert each number to a string. Finally, the elements are joined together into one string using the 'join' method.

The example usage in the docstring demonstrates the function's behavior for 'n' equal to 0 and 5, producing the expected output strings '0' and '0 1 2 3 4 5' respectively.