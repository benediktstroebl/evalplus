```python
def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:0]  # Create a new string with the same prefix as s (sliced with :0)

    for char in s:
        if char not in delete:
            palindrome += char

    return palindrome, palindrome == palindrome[::-1]

# Example usage:
s = "abcdedcba"
c = "ab"
result = reverse_delete(s, c)
print(result)  # Output: ('cdedc', True)
```

The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the modified string after deleting characters in `s` that are present in `c`, along with a boolean indicating whether the resulting string is a palindrome. To achieve this, the function constructs a new string `palindrome` where characters not present in the delete list are appended. The delete list is created from `c` by listing its characters. The function then returns the `palindrome` along with a boolean indicating whether it's a palindrome by comparing it to its reverse (`palindrome[::-1]`).

The example usage demonstrates the function's behavior using the input values `s = "abcdedcba"` and `c = "ab"` and prints the returned tuple (`cdedc`, `True`) as the output.