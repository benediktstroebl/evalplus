```python
def reverse_delete(s, c):
    # Resultant String after deletion
    result = [x for x in s if x not in c]

    # Checking if the resultant string is a palindrome
    # by comparing the first and last characters
    return (result, result[0] == result[-1])
```

This approach uses a list comprehension to create the resultant string after deletion, then a comparison of the first and last characters of the resultant string is done to determine whether it is a palindrome. This algorithm has a time complexity of O(n) where n is the length of the string and a space complexity of O(1).