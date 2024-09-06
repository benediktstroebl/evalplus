```python
def strlen(string: str) -> int:
    return len(string)

# Test the function with various inputs
assertEqual(strlen(''),            # Empty string: 0
   '',                        # Single character: 1
   'abc',                 # Multiple characters: 3
   'abcde',              # More text: 5
   'ABCDEFGHIJKLMNOPQRSTUV', # Lots of text: 6)
```
The function **strlen** calculates the length of a given string. It returns an integer value representing the value of the string length, which is based on the **len()** function that returns the length of a given string. The test cases ensure the simple checks for different inputs, such as empty strings, single characters, multiple characters, and longer texts.