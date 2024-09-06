```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
print(string_sequence(0))
```
The function 'string_sequence' takes an integer 'n' as input and returns a string consisting of space-separated numbers ranging from 0 to 'n' inclusive. The test cases demonstrate that for 0, the function returns '0'. 

As per your instructions, the code is formatted in a Markdown code block for readability and clarity. Feel free to ask if you would like me to explain any part of the code in detail.