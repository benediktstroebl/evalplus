```python
def reverse_delete(s, c):
    # Remove characters in 's' that are present in 'c'
    s = [x for x in s if x not in c]
    
    # Check if the resulting string is a palindrome
    return (s, s == s[::-1])
```

This Python script defines a function `reverse_delete` takes two strings, `s` and `c`, as input, it removes characters in `s` that are present in `c` and then checks if the resulting string is a palindrome. The function returns a tuple containing the modified string `s` and a boolean value indicating whether it is a palindrome (True if it is, False otherwise). 

To achieve this, the script utilizes list comprehension to filter out characters in `s` that appear in `c`, creating a new string that only contains the desired characters. The reverse check is conducted by comparing the modified string with its reverse using the slicing notation `[::-1]`. 

The provided code aims to solve the problem statement presented in the task, which involves removing specific characters from one string and then checking if the modified string is a palindrome.