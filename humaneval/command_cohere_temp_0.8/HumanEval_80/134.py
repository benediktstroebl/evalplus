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

The problem is solved by checking the length of the string. If it is less than 3, it obviously cannot be happy, so we return `False`. Next, we check every consecutive group of 3 letters. We use a set to store these letters, if any two of the letters match, then it's not happy and we return `False`. If not, the variable `letters_set` would have exactly 3 distinct letters, so we return `True`.

This approach gives a time complexity of `O(n)` and a space complexity of `O(n)`, where `n` is the length of the string, as we are iterating the entire string and storing 3-letter segments in a set.

Here is a test suite that proves the correctness of the function:
```python
def test_happy():
    assert is_happy("abcd")
    assert not is_happy("aabb")
    assert is_happy("adb")
    assert not is_happy("xyy")
    assert not is_happy("aaa")
    assert is_happy("abxy")
``` 
To test the function, you can run the `test_happy()` function in your Python environment.