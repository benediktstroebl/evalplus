```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

The problem is solved by checking the length of the string. If it is less than 3, it returns False, as there cannot be three consecutive letters to compare. If the length is at least 3, it checks if each set of three consecutive letters are distinct. If they are, it returns True; if not, it returns False. 

This algorithm has a time complexity of O(n) where n is the size of the input string, and a space complexity of O(1) as it only uses a constant amount of extra space to store the variables. 

To pass tests, you can create a list of test strings and compare each string to the expected output using an assert statement. Here is an example:
```python
assert is_happy("abcd") == True
assert is_happy("aabb") == False
assert is_happy("adb") == True
assert is_happy("xyy") == False
``` 
This gives you a passing test suite for the `is_happy` method. 

Let me know if I've answered your question correctly! I'm here to help if you have any other questions or concerns.