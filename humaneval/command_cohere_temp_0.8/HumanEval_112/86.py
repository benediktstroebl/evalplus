```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [char for char in s if char not in c]

    # Check if the resultant string is a palindrome
    return (''.join(result), result == result[::-1])
```

The approach for this solution is to simply filter out the characters from string `s` that are present in string `c` using a list comprehension and then checking if the resultant string is a palindrome by comparing the resultant list with its reverse using the `slicing` [::-1] technique. The overall time complexity of this approach is **O(n log n)**, where n is the length of the string `s` as string concatenation and appending (used in the list comprehension) has a time complexity of O(n log n). 

The space complexity is O(1) as in the worst case we are using constant space to store the resultant list in the list comprehension.