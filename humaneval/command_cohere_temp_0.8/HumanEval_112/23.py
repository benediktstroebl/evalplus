```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

The idea here is we take the string `s` and remove all the characters that are present in the string `c`. This gives us the first part of the answer, the second part is to check if the resulting string is a palindrome which we can do by reversing the order of the characters and comparing it to the original deleted string. We reverse the order of the characters deleting the characters of `c` by first reversing the entire string and then appending the characters that were deleted to get the string `c`. We do not in any way alter the value of s. The logic does not use the outline provided and is relatively simple to test, the code does not use any extra libraries and is a standalone Python script.