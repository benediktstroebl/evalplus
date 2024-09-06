```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    if delete == delete[::-1]:
        return delete, True
    else:
        return delete, False
```
The following tests will check if the above code works as expected:
```python
def test_reverse_delete():
    assert reverse_delete("abcdef", "b") == ("acdef", False)
    assert reverse_delete("abcde", "ae") == ("bcd", False)
    assert reverse_delete("abcdedcba", "ab") == ("cdedc", True)
    assert reverse_delete("hello", "l") == ("heo", False)
    assert reverse_delete("abab", "ab") == ("abab", False)
    assert reverse_delete("abc", "abc") == ("", True)
```
We use a list comprehension to delete characters in s that are also in c. After deleting, we reverse the remaining characters and concatenate a blank character to the end of the list to handle the case where the string has no characters left. Then we check if the list of characters is a palindrome. The tests check edge cases and ensure the function behaves as expected.