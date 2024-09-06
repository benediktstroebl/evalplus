```python
def count_upper(s):
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This approach uses a list `upper_vowels` to store all uppercase vowels, a `for` loop to iterate through the characters in the passed string `s`, and checks if the character at the current index is uppercase and a vowel, increasing the count variable if so. The loop iterates every two indices to check for even indices only. The final count is returned. 

Such problems require basic knowledge of Python, lists, loops, and string properties, along with some more advanced ideas such as checking for even indices and filtering with `isupper()` and `in`. 

Let me know if you would like me to explain any of these concepts or offer any further guidance.