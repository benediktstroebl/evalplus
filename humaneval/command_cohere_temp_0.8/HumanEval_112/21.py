```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that appear in c
    result = ''.join(x for x in s if x not in c)
    # Check if the remaining string is a palindrome
    return result, result == result[::-1]
```

The problem is solved using Python's list and string manipulation features. The function `reverse_delete()` executes the following steps:
1. Create an empty string to store the resultant values.
2. Use a list comprehension to iterate over all characters in the input string `s`, and append the characters that do not appear in the forbidden string `c` to the empty string.
3. Return the resulting string and a boolean indicating whether it is a palindrome by comparing it with its reverse.

This solution is efficient and uses minimal Python features, making it readable and easy to understand. It solves the problem by removing characters in `s` that appear in `c` and then checking if the resultant string is a palindrome.