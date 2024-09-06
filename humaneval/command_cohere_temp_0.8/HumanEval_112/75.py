```python
def reverse_delete(s, c):
    delete = [char for char in c]
    result = ''.join([char for char in s if char not in delete])
    return result, result == result[::-1]
```
The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the modified string `s` with all characters deleted that are present in `c`, and a boolean indicating whether the resulting string is a palindrome.

To solve the problem, the script uses a list comprehension to create a list of characters to delete from the original string `s` by filtering characters that appear in the string `c`. It then uses another list comprehension to construct a new string `result` by joining the characters of `s` that are not in the list of characters to be deleted. The resultant modified string is returned after the procedure. 

The boolean value is determined by whether the resulting string is a palindrome, achieved through the use of a slice notation to reverse the string and compare it with the original to determine parity.

This script may be used as a standalone solution and is compatible with a variety of test cases that adhere to the problem statement's given examples.