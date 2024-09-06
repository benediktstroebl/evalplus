```python
def reverse_delete(s, c):
    delete = [char for char in c]
    result = ''.join([char for char in s if char not in delete])
    return result, result == result[::-1]
```
This function takes two strings, s and c, as input and returns a tuple containing the result of deleting characters from s that are present in c, and a boolean indicating whether the resulting string is a palindrome. The code checks if the result string is a palindrome by comparing the backward and forward directions of the string, using the slice result[::-1] to reverse the string.

Here is a test suite that can be used to validate the function:
```python
def test_reverse_delete():
    assert reverse_delete("abcde", "ae") == ("bcd", False)
    assert reverse_delete("abcdef", "b") == ("acdef", False)
    assert reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert reverse_delete("abcdef", "abcdef") == ("", True)
    assert reverse_delete("abcd", "cd") == ("ab", False)
    assert reverse_delete("abcd", "abcd") == ("", True)
    assert reverse_delete("abc", "abc") == ("", True)
``` 
To test the function, the test suite provides different inputs and expected outputs for the function. The reverse_delete function is called with specific strings and characters, and the returned tuple is compared with the expected result. Thorough testing is performed by varying the input strings and characters, ensuring correct deletion and palindrome checking.