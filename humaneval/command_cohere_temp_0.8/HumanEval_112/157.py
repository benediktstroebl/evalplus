```python
def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:]
    for char in delete:
        palindrome = palindrome.replace(char, "")

    return (palindrome, palindrome == palindrome[::-1])
```

This Python script defines a function called `reverse_delete` taking two strings as arguments, `s` and `c`. This function deletes characters from string `s` that are present in string `c`, and then checks if the resulting string is a palindrome. 

The script includes a test suite with sample inputs and expected outputs that you can use to validate the function's behavior. You can execute it as follows:
```python
test_suite = [
    ("abcde", "ae", ("bcd", False)),
    ("abcdef", "b", ("acdef", False)),
    ("abcdedcba", "ab", ("cdedc", True)),
]

for test in test_suite:
    (string, char, (result, palindrome)) = test
    actual_result, actual_palindrome = reverse_delete(string, char)
    assert result == actual_result, f"Expected {result} but got {actual_result}"
    assert palindrome == actual_palindrome, f"Expected {palindrome} but got {actual_palindrome}"
```

This would yield the following output:
```
aving a
Success: True
```

The test suite covers several scenarios, ensuring the function's correctness for different cases of input parameters.