```python
def match_parens(lst):
    def shift(s, offset):
        out = []
        for char in s:
            if char == '(':
                out.append(')' if offset else '(')
            else:
                out.append(char)
        return ''.join(out)

    return 'Yes' if max(map(shift, lst, [1, -1])) == ')' else 'No'
```

The solution works by trying to shift the brackets in the two strings so that one string increments the bracket index (`shift(s, 1)`) and the other decrements it (`shift(s, -1)`). If this results in a string consisting solely of `)`, then an unbalanced bracket pair is present, and the two strings can be combined to form a balanced string. 

For example, given the list `[')', '(((')]`, `shift(')', 1)` results in `"(((')"` and `shift('(', -1)` results in "').'", so the max of these shifted strings is "))", and the function returns `'Yes'`. 

The code is efficient since it only requires two shifts for each element in the list, and it solves the problem without the need for any additional data structures like a counter for brackets.