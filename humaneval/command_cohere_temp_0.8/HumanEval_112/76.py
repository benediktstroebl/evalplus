```python
def reverse_delete(s, c):
    delete = [char for char in c]
    result = ''.join([char for char in s if char not in delete])
    return result, result == result[::-1]
```
This Python script defines a function `reverse_delete` taking two strings `s` and `c` as input, aiming to delete characters in `s` that are also present in `c`, and then determine if the resulting string is a palindrome. The task is accomplished in two main steps: first, a list called `delete` is created to hold the characters from string `c`, which serves as the set of characters to be deleted from string `s`. Second, a new string `result` is formed by concatenating all characters from `s` that are not present in the `delete` list. The function returns a tuple containing this `result` string and a boolean value, denoting whether the `result` is a palindrome (i.e., reading the same backward as forward).

Here is an example of how to use the `reverse_delete` function:
```python
def test_reverse_delete():
    assert reverse_delete("abcde", "ae") == ("bcd", False)
    assert reverse_delete("abcdef", "b") == ("acdef", False)
    assert reverse_delete("abcdedcba", "ab") == ("cdedc", True)

test_reverse_delete()
```

To verify the function's correctness, the `test_reverse_delete` function is employed, which utilizes the `assert` statement to validate two test scenarios, ensuring that the function's output corresponds correctly to the expected results for those inputs.

Note: This solution assumes that the input strings `s` and `c` are both lowercase for simplicity and due to the nature of the palindrome check implementation. If the input might contain uppercase characters, you may need to account for that in the palindrome check or use characters explicitly instead of their ordinals.