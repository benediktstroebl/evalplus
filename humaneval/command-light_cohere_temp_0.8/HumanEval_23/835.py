```python
def strlen(string: str) -> int:
    return len(string)

#Test case 1: Empty string
assertEqual(strlen(''), 0)

#Test case 2: Single character
assertEqual(strlen('abc'), 3)

#Test case 3: Multiple characters
assertEqual(strlen('hello world'), 13)
```  This script defines a function `strlen` that calculates the length of a given string. It is then tested with three cases: an empty string, a string with a single character, and a longer string. 

This code is self-contained and will print all the assertions if the script is executed.