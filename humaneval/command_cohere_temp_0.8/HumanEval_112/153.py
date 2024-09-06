```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    result = ''.join(char for char in s if char not in delete and char in reverse)
    return result, result == result[::-1]
```

The problem asks us to create a function `reverse_delete(s,c)` that takes two strings as input, `s` and `c`, and deletes all characters in `s` that are present in `c`. Then, it checks whether the resulting string is a palindrome and returns a tuple consisting of the resulting string and a boolean indicating whether it is a palindrome. The code starts by creating a list called `delete` that contains all the characters from the `c` string. It then creates a reversed version of the main string, `s`, and iterates through the main string, checking if each character is not in the `delete` list and is present in the reversed version of the string. The characters that meet these conditions are collected in the `result` string. The function returns a tuple of the `result` string and a boolean indicating whether it is a palindrome, checked using the condition `result == result[::-1]`. 

This solution works correctly and efficiently for the specified problem. You can add tests for this code to ensure that it behaves correctly for other cases as well. Here is a test to add to our code:
```python
def test_reverse_delete():
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert reverse_delete("abc", "abc") == ('', True)
    assert reverse_delete("aaa", "aa") == ('', True)
    assert reverse_delete("abcd", "dcba") == ('ab', False)
    assert reverse_delete("abcd", "abc") == ('d', False)
``` 
This test case covers some additional scenarios for strings of varied lengths and different characters.