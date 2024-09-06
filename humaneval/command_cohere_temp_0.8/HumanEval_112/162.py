```python
def reverse_delete(s, c):
    delete = [char for char in c]
    result = ''.join([char for char in s if char not in delete])
    return result, result == result[::-1]
```
The problem asks us to create a function `reverse_delete(s,c)` that takes two strings as input, `s` and `c`, and returns a tuple containing a modified version of `s` where all characters found in `c` have been deleted, and a boolean indicating whether the resulting string is a palindrome. 

To solve this, we use a list comprehension to create a list of characters to be deleted from `s`, based on the second input string `c`. We then use a loop to iterate through `s` and build a new string, `result`, that includes only the characters from `s` that are not in the list of characters to be deleted. The resulting string is returned as the first element of the tuple.

To determine whether the resulting string is a palindrome, it is checked whether `result == result[::-1]`, where `s[::-1]` returns a string with the elements of `s` in reverse order. The boolean value returned by this comparison is the second element of the returned tuple.

The script passes the test cases provided, including:
```python
test_cases = [
    ("abcde", "ae", "bcd", False),
    ("abcdef", "b", "acdef", False),
    ("abcdedcba", "ab", "cdedc", True),
]

for s, c, expected_s, expected_palindrome in test_cases:
    result, palindrome = reverse_delete(s, c)
    assert result == expected_s, f"For s={s} and c={c}, the expected deleted result was {expected_s}, but the actual result was {result}"
    assert palindrome == expected_palindrome, f"For s={s} and c={c}, the expected palindrome check was {expected_palindrome}, but the actual result was {palindrome}"
```
This code asserts that the `reverse_delete` function returns the expected results for various test cases.