```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

The following test cases correspond to the above code:
```python
def test_reverse_delete():
    assert reverse_delete("abcdef", "b") == ("acdef", False)
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert reverse_delete("abcdef", "abc") == ('f', True)
    assert reverse_delete("abcd", "abcd") == ('', True)
```

The `reverse_delete()` function takes two strings, `s` and `c`, as input and returns a tuple containing the result string and a boolean indicating whether the resulting string is a palindrome. It is achieved as follows:
1. The first step is to create a list comprehension that deletes all the characters in `s` that are equal to any character in `c`. This list comprehension does not reverse the order of the characters at this point.
2. Then a `reverse()` method call is applied on the resultant list which takes the deleted characters and reverses their order.
3. After that, a concatenation operation is performed on the reversed deleted string and the original deleted characters, which effectively inserts the deleted characters back into the string.
4. The final string is returned, and a comparison is performed to check whether the string is a palindrome, which is determined by the `!=` operator donning its boolean mantle, resulting in a boolean value accordingly.