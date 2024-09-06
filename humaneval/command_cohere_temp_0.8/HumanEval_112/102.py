```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that appear in c
    result = ''.join(x for x in s if x not in c)
    # Check if the resultant string is a palindrome
    return result, result == result[::-1]
```

The problem is solved using Python's list and string manipulation features. The function `reverse_delete()` executes the following steps:
1. Create an empty string to store the resultant values `result = ''`.
2. Use a list comprehension to iterate over all characters in `s`, and append them to `result` if they are not present in `c`.
3. Since all deletion operations are cumulative, the result string will contain the deleted characters.
4. Finally, the function returns a tuple containing the result string and a boolean indicating whether the result is a palindrome.

This solution leverages basic Python principles, making it concise and easily understandable. It solves the problem by removing characters and determining if the remaining string is a palindrome, efficiently.