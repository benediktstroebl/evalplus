```python
def match_parens(lst):
    def merge(a, b):
        stk = []
        for c in a + b:
            if c == '(':
                stk.append(c)
            else:
                if not stk or stk[-1] != '(':
                    return False
                stk.pop()
        return not stk
    
    return 'Yes' if merge(lst[0], lst[1]) else 'No'
``` 

This script uses a helper function `merge` to check if it's possible to merge two strings in some order and still maintain balanced parentheses. The main function `match_parens` takes a list of two strings as input and utilizes the `merge` function to determine whether the two strings can be merged. If it is possible, the function returns `"Yes"`, and `"No"` otherwise. 

This solution follows the **dynamic programming** approach, wherein we break the problem into smaller sub-problems and solve them in a recursive manner. Here, the sub-problems are formed by the pairs of strings created from the input list.