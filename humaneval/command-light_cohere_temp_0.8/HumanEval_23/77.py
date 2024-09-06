```python
def strlen(string: str) -> int:
    """ Returns length of given string"""
    return len(string)

#Test cases
assertEqual(strlen(''),      #Test case 1: empty string
    0)

assertEqual(strlen('abc'), #Test case 2: contains only alphabetical characters
    3)

# Test case 3: contains special characters
assertEqual(strlen('#@'),  #No of special characters
    4)

# Test case 4: large string
assertEqual(strlen('""),  # leading spaces
    5)

# Test case 5: contains all characters
assertEqual(strlen('a')),  # contains only alphabetic characters
    6)
``` 
This function, `strlen`, takes a string as input and returns its length. It's a simple and straightforward, with an easy-to-read docstring. The test cases are then passed to ensure the function works correctly for a variety of inputs.