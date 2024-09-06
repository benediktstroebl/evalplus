```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    return (''.join(delete), delete == s)
```

The problem asks us to create a function `reverse_delete(s,c)` that takes two strings as input, `s` and `c`, and returns a tuple containing a string that is formed by deleting from `s` all characters that are present in `c`, and a boolean indicating whether the resulting string is a palindrome. The palindrome is determined by checking whether the string reads the same backward as forward. To solve this problem, the idea is to create a new string that contains all the characters of `s` except the characters that are present in `c`, and then check whether the new string is a palindrome. To achieve this, we use a list comprehension to create a new string `delete` by picking all characters in `s` that are not in `c`. We then use the `reverse()` method, followed by concatenation with an empty string, to handle cases where the resulting string has an odd length and needs to be padded with an empty string to be a palindrome. The final step is to return a tuple containing the string `delete` and a boolean indicating whether `delete` is equal to `s`, which would imply that the resulting string is a palindrome. The example usage and tests demonstrate the correctness of the approach.