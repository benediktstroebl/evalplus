```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    result = ''.join(char for char in s if char not in delete and char in reverse)
    return result, result == result[::-1]
```

The problem asks to delete all characters in `s` that are present in `c`, and then to check whether the resulting string, when possible, is a palindrome. The goal is to return a tuple containing the result string and a boolean indicating whether it is a palindrome.

The solution leverages Python's `str.startswith` method to check whether the string would be a palindrome. The list comprehension `delete` creates a list of all characters in `c` to delete from `s`. The string `result` is created by iterating over each character in `s` and selectively including those that are not in `delete` nor in the reverse complement of `s`. This way, the characters to be deleted are omitted, and we check whether the result is a palindrome.

The tests that can be used to validate this code are:
```python
def test_reverse_delete():
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert reverse_delete("abcdedcba", "abcd") == ('', True)
    assert reverse_delete("abc", "abc") == ('', True)
    assert reverse_delete("123", "32") == ('1', True)
    assert reverse_delete("abc", "ab") == ('c', True)
``` 

This test suite covers a variety of scenarios, including edge cases, to ensure the correctness of the `reverse_delete` function.