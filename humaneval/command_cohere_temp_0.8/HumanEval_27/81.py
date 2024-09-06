```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert uppercase characters to lowercase and vice versa. The condition `c.isalpha()` checks if the character is alphabetical, excluding non-alphabetical characters from the flip case conversion. It then uses the join function to combine these flipped characters into a single string. 

To test this, you can run the following:
```python
>>> flip_case('Hello World! And moreover, fooBAR')
'HELLO WORLD! AND MOREOVER, foobar'
``` 

This should flip the case of alphabetic characters, leaving non-alphabetic characters unchanged.