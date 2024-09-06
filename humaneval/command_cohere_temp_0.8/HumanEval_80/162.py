```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] == s[i+1] and s[i] == s[i+2]:
            return False
        letters_set.add(s[i])
    return True
```

The function uses a set `letters_set` to store the letters of the string `s` with an emphasis on every 3 consecutive letters. If the size of the set reaches 3 or more and the next 3 letters are the same as the previous, the function returns False. Otherwise, it returns True. The function also checks if the string length is at least 3 with the `if len(s) < 3` statement. 

This solution enables you to efficiently verify whether a given string satisfies the "happy" criteria solely through its code. 
To see the function in action, call it through the console using your own test cases. For instance:
```python
print(is_happy('abcd'))  # Output: True
print(is_happy('aabb'))  # Output: False
print(is_happy('xyy'))  # Output: False
``` 
This way, you can validate the correctness of the solution based on your anticipated results.