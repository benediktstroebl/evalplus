```python
def reverse_delete(s, c):
    # Resultant String after deletion
    result = [x for x in s if x not in c]

    # Checking if the resultant string is a palindrome
    # By comparing the two ends of the string
    return (''.join(result), result == result[::-1])
```

The approach for this solution is to simply filter out all the characters from string `s` that are present in string `c` using the list comprehension and creating a new string by joining the resultant list. Then, to check if the resultant string is a palindrome, we compare the first character of the string to the last character of the string and so on for the remaining characters. If the string is equal to the reversed string, it is a palindrome. Otherwise, it is not. 
This solution's time complexity is O(n m) where n is the length of string s and m is the length of string c.