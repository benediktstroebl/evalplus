```python
def match_parens(lst):
    def merge(a, b):
        depth_a = 0
        depth_b = 0
        curr = ''
        res = ''
        for c in a + b:
            if c == '(':
                if curr == ')':
                    res += ')'
                    depth_b -= 1
                else:
                    res += c
                    depth_a += 1
            elif c == ')':
                if curr == '(':
                    res += ')'
                    depth_a -= 1
                else:
                    res += c
                    depth_b += 1
            curr = c
        if max(depth_a, depth_b) == 0:
            return 'Yes'
        else:
            return 'No'

    if len(lst) != 2:
        return 'No'
    else:
        return merge(lst[0], lst[1])
```

The code defines a function `match_parens` that takes in a list of two strings, each containing only open parentheses `'('` or close parentheses `')'`. It then checks if it's possible to concatenate the two strings in some order to form a balanced parentheses string. 

The function uses a helper function `merge` that accepts two strings and repeatedly compares the characters at the front of the strings. It shifts the parentheses to form a balanced string as it goes. After walking through the strings, if the maximum depth is 0, it means all parentheses are matched, and the result is 'Yes'. Otherwise, the result is 'No'.

In the provided implementation, the code first checks if the input list has 2 elements (as required). If not, it returns 'No'. Otherwise, it uses the `merge` function to determine if a balanced string can be formed and returns 'Yes' or 'No'. The overall time complexity is O(mn) where m, n are the lengths of the two input strings.