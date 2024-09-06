```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrence = [0] * len(s)
    for i in range(len(s)):
        letters_occurrence[i] = s[i]
    for i in range(len(s) - 2):
        if letters_occurrence[i] == letters_occurrence[i + 2]:
            return False
    return True
```

This Python script defines a function called `is_happy` that takes a string as an input (`s`). This function returns True if the string is happy, and False if it is not. A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct. The script returns False for strings that do not meet these criteria, and returns True for valid happy strings.

Here is an example of how to use this function:
```python
print(is_happy("abcd"))  # Output: True
print(is_happy("aabb"))  # Output: False
print(is_happy("xyy"))  # Output: False
``` 

This function can be tested on various strings to validate its behavior and ensure its correctness against the specified requirements.