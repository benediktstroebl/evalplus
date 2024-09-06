```python
def flip_case(string: str) -> str:
    """
    Converts all character to their case-reversed.
    i.e flip_lower case strings
   's all lowercase characters to uppercase, and all uppercase characters to lowercase.
    """
    string = 'hello'
    #print(string)
    return string. 
   
    # Test string
    is flipped correctly
    assert string == 'HELLO'
    # Test all characters in a string are case-flipped
    assert flip_case('hello123') == 'HELL123'
    # Test all uppercase letters are converted to lowercase
    assert flip_case('aaBBccDD') == 'aaBccDd'
    # Test all lowercase letters are converted to uppercase
    assert flip_case('hello World') == 'WORLD HELLO'
    ```