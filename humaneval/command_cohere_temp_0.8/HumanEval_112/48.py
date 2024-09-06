```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [char for char in s if char not in c]

    # Check if the remaining string after deletion is a palindrome
    # By checking the length of the string after deletion,
    # if it is equal to the length of the string before deletion, it is a palindrome
    return result, len(result) == len(s)
```

The approach uses simple Python list comprehension to filter out the characters present in `c` from `s` and then checks if the deleted string is a palindrome by comparing the length before and after deletion of characters.

This approach would result in a time complexity of O(n m) where n is the length of s and m is the length of c as it involves iterating over both strings. However, it only needs a single pass to achieve the result, thereby making it an efficient solution. 

This problem can be solved using a variety of methods and depending on the complexity of characters in `s` and `c`, different approaches can be optimized accordingly. 

This approach results in a concise and elegant solution to the problem.