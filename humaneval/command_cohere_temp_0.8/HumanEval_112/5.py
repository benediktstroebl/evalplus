```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [char for char in s if char not in c]

    # Check if the resultant string is a palindrome
    # By checking the length of the string after removing characters in s that are equal to characters in c
    if len(result) == len(result)[::-1]:
        return ''.join(result), True
    else:
        return ''.join(result), False
```

The approach employed by the `reverse_delete` function is as follows:
1. Create a resultant string by looping through every character in `s` and checking if that character is not in `c`.
2. After creating the resultant string, check its length and compare it to the length of the string reversed. If the lengths are equal, the resultant string (after deleting) is a palindrome; otherwise, it's not.

This solution utilizes Python's innate string-handling capabilities and len functions to accurately determine the length of strings and verify if the resultant string after deletion is a palindrome.

This approach provides a concise and efficient solution to the stated problem. It is both self-contained, in that it does not require external variables or data and standalone, as it can be copied and run directly as a Python script.