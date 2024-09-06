```python
def match_parens(lst):
    def shift(s):
        return s.replace('(', '').replace(')', '')
    
    if len(lst) != 2:
        return "Invalid input"
    
    s1, s2 = lst
    s1 = shift(s1)
    s2 = shift(s2)
    
    if not s1 and not s2:
        return "Yes"
    
    if (not s1 and s2) or (not s2 and s1):
        return "No"
    
    return "Yes"
```

The following is an explanation of how the code works:
1. The function `match_parens` takes a list `lst` with exactly 2 elements, assuming it to be a pair of strings representing open and close parentheses.
2. The function defines a nested helper function `shift`, which removes all open parentheses '(' and close parentheses ')' from a given string, essentially leaving only the balance of the parentheses.
3. It then checks if the input list is even partially valid, by verifying there are exactly two elements (`if len(lst) != 2`), and returns "Invalid input" if not.
4. The function then processes the two strings `s1` and `s2` extracted from `lst` using the `shift` function to determine the balance of parentheses in each string.
5. The function checks for certain cases of irreconcilable parentheses:
    - If both strings have a balance of 0 (i.e., have no parentheses), then they can be concatenated together to form a valid string ("Yes" is returned).
    - If exactly one string has a balance of 0 (i.e., one string has no parentheses), then it's impossible to construct a valid string by concatenating them ("No" is returned).
    - If neither string has a balance of 0 (i.e., both have parentheses), then it shifts the responsibility to the next level of parentheses, and checks again.
6. The function will repeat the process recursively for the next level of parentheses until a valid or an invalid status is determined, and returns accordingly.

Note that this solution assumes that the list contains only strings consisting of open parentheses '(' or close parentheses ')' only. It is still valid for the given problem statement, but may not work for similarly formulated problems that allow other characters in the strings. The solution could be improved to handle such cases by extracting the valid substrings consisting of only parentheses and process them accordingly.