```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that appear in c
    result = ''.join(x for x in s if x not in c)
    # Check if the remaining string is a palindrome
    return result, result == result[::-1]
```

The problem asks us to create a function `reverse_delete(s,c)` that takes two strings as input, `s` and `c`. This function must delete all the characters in `s` that are present in `c` and then return the remaining string along with a boolean indicating whether this resultant string is a palindrome. Our approach is to simply iterate over each character in `s` and check if it is not in `c` before including it in the resultant string, `result`. We then iterate over `result` and check if it is the same when iterated through in reverse order, returning a tuple of (`result`, `result == result[::-1]`).

This algorithm has a time complexity of O(n + m) where n is the length of string s and m is the length of string c, making it efficient enough to solve this problem.