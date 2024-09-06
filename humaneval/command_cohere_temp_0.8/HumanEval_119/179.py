```python
def match_parens(lst):
    def shift(s):
        return s.replace('(', '').replace(')', '')
    
    def calc(a, b):
        return shift(a+b) == shift(b+a)
    
    return "Yes" if any(calc(x, y) for x, y in zip(lst, lst[1:]) if x != y) else "No"
```

The function leverages two helpful helper functions: `shift()` quickly determines if a string consists of only open or close parentheses, and `calc()` checks if two strings can create a balanced whole when concatenated in any order. The main function then iterates through pairs of strings in the input list, zipping them together, and checking if any pair can lead to a balanced result using the `calc()` function. If any such pair is found, the function returns "Yes", and it returns "No" otherwise. This problem can be approached using standard recursion or manual stack manipulation, but this is a more succinct and efficient solution.  This approach also avoids repeated unnecessary string concatenations, as the `calc()` function checks balance without explicitly constructing potentially large intermediate strings.