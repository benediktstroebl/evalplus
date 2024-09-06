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
    else:
        return (''.join(pm), False)
```
This Python script defines a function called `reverse_delete` takes strings `s` and `c` as input, aims to delete characters in `s` that are present in `c`, and then determine if the resulting string is a palindrome. To accomplish this, it constructs a list called `delete` containing characters from `c`, iterates through the characters of `s`, and adds unaffected characters to the `pm` list. After processing, it checks if the modified string (`pm`) is the same when reading forward and backward, returning a tuple containing the modified string and a boolean value indicating whether it's a palindrome. 

The code tests are:
```python
def test_reverse_delete():
    # Test Case 1
    input1 = "abcde"
    input2 = "ae"
    expected1 = ('bcd', False)
    result = reverse_delete(input1, input2)
    assert result == expected1

    # Test Case 2
    input1 = "abcdef"
    input2 = "b"
    expected2 = ('acdef', False)
    result = reverse_delete(input1, input2)
    assert result == expected2

    # Test Case 3
    input1 = "abcdedcba"
    input2 = "ab"
    expected3 = ('cdedc', True)
    result = reverse_delete(input1, input2)
    assert result == expected3

test_reverse_delete()
```

When you execute the code, the test suite will run three tests, and the output will indicate whether the tests pass.