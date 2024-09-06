```python
def solve(s):
    new_str = []
    for c in s:
        if c.isalpha():
            new_str.append(c.swapcase())
        else:
            new_str.append(c)
    return ''.join(new_str)
```

This script defines a function `solve` taking one parameter `s`, which performs the desired operations as specified in the problem statement. 

The function first creates a new string `new_str` to store the result. Then, it iterates through each character `c` in the input string `s`. 

For each character, it checks if the character is an alphabet letter using the method `isalpha()`. If it's an alphabet letter, it uses the method `swapcase()` to change the case of the character (upper to lower or vice versa). Otherwise, if the character is not an alphabet letter, it appends the character as it is. 

Finally, the function returns the resulting string by joining the elements in the `new_str` string. 

This solution is efficient and straightforward, achieving a time complexity of O(n), where n is the length of the input string `s`.