```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The function uses a trick where we consider all 3 consecutive letters to be in a single set. Then we check if the size of this set is 1 (meaning it contains only distinct letters), and if the total size of the set is equal to the size of the string minus 2 (the two ends of the sequence accounted for in the total size minus the consideration of the 3 consecutive letters as one element). 

The following is a test that can be used to validate the function:
```python
# tests
assert is_happy("abcd")
assert not is_happy("aabb")
assert is_happy("adb")
assert not is_happy("xyy")
assert not is_happy("aaa")
``` 
If you would like more tests for this function, or would like more detailed explanations of the function or tests, let me know!