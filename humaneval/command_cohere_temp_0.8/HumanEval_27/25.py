```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as input and returns a new string where all alphabetic characters have been flipped between lowercase and uppercase. The `swapcase` method is utilized for this flipping, while non-alphabetic characters are left unchanged. 

To verify the functionality, you can run the test case provided like so:
```python
>>> flip_case('Hello World')
'hELLO WORLD'
``` 

This should return 'hELLO WORLD' as the result, where only the alphabetic characters have been flipped in case. 

Let me know if you would like me to explain any part of the code in more detail. I can highlight specific aspects of it if needed.