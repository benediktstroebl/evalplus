Here's a Python function that checks if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if text is same when reading forward and backward
    return text == text[::-1]
```
This function first removes all non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. It then uses slicing to reverse the text and checks if it's the same as the original text. The function returns True if it's a palindrome and False otherwise. 

Here's how you can use it and run the provided tests:
```python
import unittest

def test_is_palindrome():
    unittest.main(testRunner=unittest.TextTestRunner())

test_is_palindrome()
```
Note: The `test_is_palindrome()` function is provided to facilitate the execution of the tests. However, to run the tests correctly, it is necessary to execute the cell twice, as the first execution only defines the tests but does not run them. To avoid this step, you can use the `unittest` module directly in your code to define and run the tests as shown below:
```python
import unittest

def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if text is same when reading forward and backward
    return text == text[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(is_palindrome(''))

    def test_palindrome(self):
        self.assertTrue(is_palindrome('aba'))

    def test_long_palindrome(self):
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

if __name__ == '__main__':
    unittest.main()
```