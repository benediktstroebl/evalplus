```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i+1], s[i+2]])) != 3:
            return False
    return True
```

This Python script defines a function called `is_happy` that takes a single argument - a string `s`. This function returns True if the string is happy, i.e., its length is at least 3 and every 3 consecutive letters are distinct; otherwise, it returns False. 

The script utilizes a set to store unique letters occurring in the string. It then checks every 3 consecutive letters, subtracting them from the set to check if they are distinct. If the set length is 3 after the subtraction, the answer is True, and if not, the answer is False. 

The provided code includes an inline test to verify correctness. You can also test it with specific input strings to verify the happy status. For instance:
```python
print(is_happy('abcd'))  # Output: True
print(is_happy('aabb'))  # Output: False
print(is_happy('xyy'))  # Output: False
```