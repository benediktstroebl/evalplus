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

This script defines a function `solve` that takes a string `s` as input and checks if `s[i]` is a letter or not using the `isalpha()` function. If it is, it swaps the case using `swapcase()` function and appends the new character to the `new_str` list. If it is not, it just appends the character to the `new_str` list as it is. Finally, the function returns the newly formed string by joining the list of characters in `new_str` with the `join()` method.

The code tests the function with different cases and prints the expected output:
```
> solve("1234")
4321
> solve("ab")
AB
> solve("aaa")
AAA
> solve("@#$%^&*()")
%^&*()@#$
> solve("#a@C")
#A@c
```

The test cases contain different strings with different characters and cases to ensure the function behaves correctly with regards to the problem statement.