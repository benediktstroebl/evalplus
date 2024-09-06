```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i+1])] > 1 or letters_count[ord(s[i+2])] > 1:
            return False
    return True
```

The code first checks if the string's length is at least 3, then it counts the occurrences of each letter in the string using a 128-element array, and checks if any letter occurs more than once in any substring of length 3.

To use this function, just define the string you want to test it with, like this:
```python
string = 'xyy'
happy = is_happy(string)
print(happy)
``` 
The code will then print `False`, as the string `xyy` is not happy due to the repetition of the 'y' character.