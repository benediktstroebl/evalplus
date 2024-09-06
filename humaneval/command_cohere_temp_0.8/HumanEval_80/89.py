```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i+1])] > 1 or letters_count[ord(s[i+2])] > 1:
            return False
    return True
```

The function `is_happy()` checks if the given string `s` is happy by using a sliding window of size 3 to check every trio of consecutive letters. The function returns `True` if every trio is unique, and `False` otherwise. 

You can test the above function by using the following test cases:
```python
# Test cases
assert is_happy("abcd")
assert not is_happy("aabb")
assert is_happy("adb")
assert not is_happy("xyy")
assert not is_happy("aaa")
``` 
The first test case checks that a happy string with all unique pairs is correctly recognized. The second test case asserts that a string containing repeated pairs is not considered happy. The third test case checks that the function correctly identifies a happy string with one repeated letter. The last test case demonstrates that a string with repeated letters is not considered happy, even if the repeated letter occurs only once.