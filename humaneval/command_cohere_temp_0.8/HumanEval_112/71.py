```python
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]
```
The above function deletes characters in string `s` that are present in string `c`, and then checks if the resulting string is a palindrome. The deletion process is done within a list comprehension, and the joined string is checked for palindrome using slicing (`s[::-1]`) which reverses the string and checks for equality. The function returns a tuple containing the resulting string and a boolean indicating whether it's a palindrome. 

Here's a usage example: 
```python
print(reverse_delete("abcde", "ae")) 
# Output: ('bcd', False)

print(reverse_delete("abcdef", "b")) 
# Output: ('acdef', False)

print(reverse_delete("abcdedcba", "ab"))
# Output: ('cdedc', True)
``` 
The function passes the test cases as expected, as it successfully reverse deletes the characters and determines whether the resulting string is a palindrome.