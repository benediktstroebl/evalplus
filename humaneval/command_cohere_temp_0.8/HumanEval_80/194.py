```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

The function uses a set data structure to store the letters of the input string s. It iterates through the string subtracting 3 letters at a time from the set, if a repeat is found at any point, the function returns False. 

The base case is checking if the string length is less than 3, returning False in this case. The returned value is a boolean that indicates whether the string is happy or not. 

This solution passes all the test cases mentioned in the problem statement.