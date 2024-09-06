```python
def reverse_delete(s, c):
    delete = [char for char in c]
    result = ''.join([char for char in s if char not in delete])
    return result, result == result[::-1]
```
The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the result of deleting characters from `s` that are present in `c`, and a boolean indicating whether the resulting string is a palindrome. 

To solve the problem, the script uses a list comprehension to create a `delete` list that contains all the characters from the second string `c`. It then uses a generator expression to iterate over the characters of the first string `s`, selectively appending each character to the result string if it is not in the `delete` list. The resulting string is then returned, and a boolean value is returned based on whether the result is a palindrome. This is done using the slice notation `result[::-1]` to reverse the string and compare it to the original result.

The code above is self-contained and should run correctly as long as the variables `s` and `c` are properly defined and of the correct data types. 

Let me know if you need anything else!