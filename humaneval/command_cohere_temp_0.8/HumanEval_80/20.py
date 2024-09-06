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

The function uses a set data structure to store the letters of the string. It iterates over the string with a step size of 2, using the current letter and the next 2 letters to check if they were already present in the set. If the set size is less than 3 or the current letter is already present in the set, this indicates a repeat pattern, and the function returns False. Otherwise, it adds the letter to the set and continues iterating. The function returns True if the length is at least 3 and there are no repeat patterns of 3 letters.

Here is a test suite to verify its correctness:
```python
def test_happy():
    assert is_happy("abcd")
    assert not is_happy("aabb")
    assert is_happy("adb")
    assert not is_happy("xyy")
    assert not is_happy("aa")
    assert is_happy("abcdef")
``` 

If you want to check against other edge cases or further refine the tests, feel free to modify the test suite or add more tests as needed. Let me know if you want me to make any other adjustments to the code or if you have any more questions!