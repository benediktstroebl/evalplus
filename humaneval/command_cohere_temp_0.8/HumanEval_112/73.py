```python
def reverse_delete(s, c):
    delete = [char for char in c]
    result = ''.join([char for char in s if char not in delete])
    return result, result == result[::-1]
```
The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the modified string `s` with all characters deleted that are present in `c`, and a boolean indicating whether the resulting string is a palindrome. 

To solve the problem, the script uses a list comprehension to create a `delete` list that contains all the characters from the `c` string. It then uses a modified string concatenation (`''.join()`) to create a new string, `result`, that consists of the characters in `s` that are not in the `delete` list. The boolean value is then checked if the `result` is a palindrome using slicing with the step of `-1` to compare the string with its reverse. 

This script offers a clear and concise solution to the problem posed, ensuring that the characters in `s` are correctly deleted when also checking for the palindrome aspect.