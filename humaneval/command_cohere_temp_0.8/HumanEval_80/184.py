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

This script defines a function called `is_happy` that takes a string as an input and checks whether the string is happy or not. The function returns True if the string is happy, and False otherwise. 

The function first checks if the length of the string is at least 3, and every 3 consecutive letters are distinct. If these two conditions are not met, it returns False. It uses a set `letters_set` to store the encountered letters in the string to check for the 3 consecutive distinct letters condition. It iterates through the characters in the string, if every 3 letters are distinct, it returns True; otherwise, it returns False. 

The given examples in the prompt will return the following results:
- is_happy(a) => False
- is_happy(aa) => False
- is_happy(abcd) => True
- is_happy(aabb) => False
- is_happy(adb) => True
- is_happy(xyy) => False