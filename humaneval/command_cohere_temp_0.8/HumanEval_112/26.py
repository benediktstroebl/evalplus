```python
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]
```

The problem asks us to create a function `reverse_delete(s,c)` that takes two strings as input, `s` and `c`. The function removes characters from string `s` that are present in string `c`, and then checks whether the modified string `s` is a palindrome. 

In the provided solution, the first step is to filter out the characters from `s` that are present in `c` by using a list comprehension and a for loop:
```python
s = [x for x in s if x not in c]
```

This creates a new string `s` from the characters that were not deleted. To avoid discrepancies between the input string's encoding and the Python interpreter's internal representation, the list is converted back to a string using ` '.join(s)'`. 

The following step is to compare the modified string to its mirror image to determine whether it is a palindrome:
```python
s = ''.join(s)
return s, s == s[::-1]
```

The whole process is encapsulated in a straightforward, easy-to-understand function that can be run independently. 

To efficiently remove characters from a string, utilizing string membership tests in Python, which are usually slower than lists, is not the most efficient solution. Converting the input strings to lists for processing might provide a performance boost in some situations. However, because the issue statement implies that the inputs are strings, the given solution optimizes for simplicity and clarity.