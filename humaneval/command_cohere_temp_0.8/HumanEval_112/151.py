```python
def reverse_delete(s, c):
    delete = [char for char in c]
    pm = []
    for i in s:
        if i not in delete:
            pm.append(i)
    pm = pm[::-1]
    if pm == s:
        return ('', True)
    elif pm == s[::-1]:
        return ('', False)
    else:
        return (pm, False)
```

This Python script defines a function called `reverse_delete` takes strings `s` and `c` as input, aims to delete characters in `s` that are present in `c`, and then determine if the resulting string is a palindrome. The function returns a tuple containing the modified string and a boolean value indicating whether the string is a palindrome after deleting the characters from `c`.

Here is an example of function usage:
```python
def test_reverse_delete():
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)

test_reverse_delete()
```