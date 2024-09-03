```python
def reverse_delete(s, c):
    # removing characters that match
    new_str = []
    for char in s:
        if char != c:
            new_str.append(char)
   
    new_str = ''.join(new_str)

    # check for palindrome
    reversed_str = ''.join(reversed(new_str))
    return (new_str, reversed_str == new_str)

# example usage
s = "abcdef"
c = "b"
result = reverse_delete(s, c)
print(result)
 ```