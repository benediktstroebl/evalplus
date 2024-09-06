```python
def reverse_delete(s, c):
    # Resultant String after deletion
    result = [x for x in s if x not in c]
    # Check if the resultant string is a palindrome
    # By concatenating the reversed string to itself
    if result == result[::-1]:
        return ''.join(result), True
    else:
        return ''.join(result), False
```

The function `reverse_delete()` takes in two strings, `s` and `c`, and returns a tuple containing the result of deleting characters from `s` that are present in `c`, and a boolean indicating whether the resultant string is a palindrome. The `result` list comprehension deletes all characters in `s` that are present in `c`, and the boolean value is determined by checking `result` for symmetry. 

This solution employs only native Python functionalities and is thus both efficient and easy to interpret. It should handle all scenarios described in the problem statement.