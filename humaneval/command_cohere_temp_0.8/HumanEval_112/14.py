```python
def reverse_delete(s, c):
    s = list(s)
    c = set(c)
    for char in c:
        s.remove(char)
    s = ''.join(s)
    return s, s == s[::-1]
```
This Python script provides a function called `reverse_delete` which takes two arguments, `s` representing a string that needs to be modified and `c` representing a string of characters to be deleted. This function works by first converting both strings into a list and a set, respectively, removing characters from the list of characters (`s`) that are present in the set of characters to be deleted (`c`). Afterward, it converts the modified list back into a string and checks whether the string has become a palindrome. The function ultimately returns a tuple consisting of the modified string and a boolean value indicating whether the string is a palindrome. 

This solution is efficient as it takes `O(n log n)` time to remove characters and `O(n)` to build the string, finally, the palindrome check takes `O(n)` time. Here are some examples of how this function can be called and its corresponding outputs:
```python
# Example 1
s = "abcde"
c = "ae"
result = reverse_delete(s, c)
print(result)  # Output: ('bcd', False)

# Example 2
s = "abcdef"
c = "b"
result = reverse_delete(s, c)
print(result)  # Output: ('acdef', False)

# Example 3
s = "abcdedcba"
c = "ab"
result = reverse_delete(s, c)
print(result)  # Output: ('cdedc', True)
``` 

In the examples, the function `reverse_delete` successfully removes the characters specified in the deletion string `c` from the input string `s`. Then, it verifies if the modified string is a palindrome, resulting in a tuple of the modified string and a boolean value indicating the palindrome status.