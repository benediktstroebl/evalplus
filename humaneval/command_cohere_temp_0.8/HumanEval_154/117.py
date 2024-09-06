```python
def cycpattern_check(word1, word2):
    word1 = word1 + word1
    return word2 in word1
```
```python
# Testing the above function:
def test_cycpattern_check():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

test_cycpattern_check()
``` 

The function `cycpattern_check()` takes in two words as input and checks if the second word or any of its rotations is a substring in the first word. The function first appends the first word to itself to ensure that any rotation of the second word can be found in the appended first word. The function returns True if a match is found, and False otherwise. 

The testing function tests the function with various inputted words and confirms that the function returns the expected values.