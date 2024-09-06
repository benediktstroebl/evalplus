```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz':]
```
The function takes a string and checks if it contains any letters, if it doesn't contain any letters, it simply swaps the case of the string, if it does contain letters, it swaps the case of the letters only. This behaviour is controlled by a conditional (]: ...) in the string.split() method which applies the swapcase() function to characters only where the condition is true.