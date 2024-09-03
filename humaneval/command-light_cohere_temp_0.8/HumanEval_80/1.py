Here's a self-contained Python function that checks if a given string is happy or not, based on the provided definition:
```python
def is_happy(s):
    """
    Checks if a string is happy or not. 
    A string is happy if its length is at least 3 and 
    every 3 consecutive letters are distinct.
    """
    string is a sequence of three distinct letters, and no other letter appears consecutively.
    :param s: str to check
    :return: boolean
    """
    # Your implementation here
    # Check if the length of the string is 3
    if len(s) < 3:
        return False

    # Initialize a flag to track whether the next three characters are distinct
    flag = True

    # Iterate over the string
    for i in range(0, len(s)-2):
        char1 = s[i]
        char2 = s[i+1]
        char3 = s[i+2]

        # Check if the next three characters are distinct
        if char1 == char2 or char1 == char3 or char2 == char3:
            flag = False
        # If three distinct characters, the string is happy
        if flag:
            return True

    return False
```

The function takes a string `s` as input and returns a boolean value indicating whether the string is happy or not. The function checks if the string length is at least 3, and every 3 consecutive letters are distinct. The function uses a `flag` to keep track of whether the next three characters are distinct. If the flag is set, it means the string has distinct consecutive characters and therefore is happy.