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

The following tests will check if the function correctly determines whether a given string is happy or not.

```python
# test if the length of the string must be at least 3
assert is_happy("ab") == False

# test if the string is happy if every 3 consecutive letters are distinct
assert is_happy("axx") == True

# test if the function returns False if the string is not happy
assert is_happy("aabb") == False
```

If you want to check whether the script will correctly solve the problem, you can uncomment one of the tests and run it. 

```python
# uncomment the following line to run one of the tests
# assert is_happy("axx") == True
``` 

This will verify if the function `is_happy()` operates appropriately.  If the test passes, you will get the following result: 
```
True
``` 

If the test will not pass, the function does not correctly solve the task or requires an additional check.  You will have to redo the code and test it again to ensure that it works correctly.