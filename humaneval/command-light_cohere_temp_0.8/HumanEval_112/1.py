```python
def reverse_delete(s, c):
    removed = set()
    for char in s:
        if char in c:
            removed.add(char)
    s = s.replace(char, "")
    if set(removed) == set(c):
        return (''.join(), True)
    return (''.join(), False)

# Example test
test_case = ['abcdef', 'b']
result, is_palindrome = reverse_delete(test_case, test_case[1])
print(f"Result: {result}, {is_palindrome}")
```
The function `reverse_delete` takes two parameters, `s` and `c`. The function iterates through the string `s` and checks if each character is also present in `c`. If a character is found in both strings, it is removed from `s` using the `remove()` method. The modified string `s` is then compared with `c` using the `is_palindrome` function. The function returns a time whether the result of the function is a tuple containing the modified string and a boolean value indicating whether the modified string is a palindrome. The function also includes example test cases to demonstrate the usage.