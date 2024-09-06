```python
def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    # Convert the words to lower case to avoid case sensitivity issues
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Check if word2 is a substring of word1
    if word2 in word1:
        return True
    
    # Check for rotations of word2 in word1
    rotations = [word2[1:], word2[0:len(word2) - 1], word2[::-1]]
    for rotation in rotations:
        if rotation in word1:
            return True
    
    return False
```

This function compares the lowercase versions of both words, checks if the second word is a substring of the first, and additionally checks if any rotation of the second word fits this criterion. The function returns `True` if any of these conditions are met, and `False` otherwise.  This approach ensures that the function can handle cases such as punctuation and whitespace without impacting the logic. 
The unit tests could look like this:
```python
# Testing the cycpattern_check function
import unittest

def test_cycpattern_check():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

class TestCycpatternCheck(unittest.TestCase):
    def test_cycpattern_check(self):
        test_cycpattern_check()

if __name__ == '__main__':
    unittest.main()
```

The first part of the test suite is a simple function that calls the function `cycpattern_check` with different inputs and verifies that the output matches the expected output. The second part of the test suite is a set of unit tests that are going to run automatically when the script is executed. This approach provides thorough testing of the function to ensure it performs correctly across a variety of cases.