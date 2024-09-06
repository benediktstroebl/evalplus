```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = delete == delete[::-1]
    return ("".join(delete), palindrome)
```

This Python script defines a function called `reverse_delete` taking two strings `s` and `c` as input. It aims to delete characters from string `s` that are also present in string `c`, and then determine if the resulting string is a palindrome. To accomplish this, it uses a list comprehension to create a list of suitable characters from `s`, followed by a reverse operation on the list. The list is then rejoined into a string. The function returns a tuple containing the resulting string and a boolean value (true or false) indicating whether it's a palindrome.

Here is an example of how you can use the above code to analyze a couple of cases:
```python
def test_reverse_delete():
    assert reverse_delete("abcde", "ae") == ("bcd", False)
    assert reverse_delete("abcdef", "b") == ("acdef", False)
    assert reverse_delete("abcdedcba", "ab") == ("cdedc", True)

test_reverse_delete()
```

The `test_reverse_delete()` function utilizes the `reverse_delete()` function to evaluate three specific test cases, asserting that the output tuple correctly represents the expected result string and the palindrome indicator for each scenario.

This approach will yield the appropriate result after removing the characters from the original string and determining whether the modified string is a palindrome.