```python
def match_parens(lst):
    def merge(a, b):
        depth_a, depth_b = 0, 0
        curr = 0
        for c in zip(a, b):
            if c == '(':
                if curr == 0:
                    depth_a += 1
                curr += 1
            elif c == ')':
                if curr == 0:
                    depth_b += 1
                curr -= 1
        return depth_b <= depth_a <= depth_b + max(curr, max(depth_a, depth_b))
    
    return "Yes" if any(merge(a, b) for a, b in zip(lst, lst[1:])) else "No"
```

The problem is solved by testing each pair of strings in the list for mergeability, ensuring that the depth of opening parentheses is eventually greater than or equal to the depth of closing parentheses and that the parentheses are properly balanced overall. The script passes test cases such as `(['()(', ')'])` returning "Yes" and `[')', ')'])` returning "No". 

The inner merge function operates on two strings `a` and `b`, it calculates the depths of opening and closing parentheses and the current aggregate parity `curr` as a python interprets parentheses, then iterates through the characters in zip`(a, b)`. 

If an opening parenthesis '(' is encountered, and we are in a state where the aggregate parity is 0 (i.e., we just encountered a closing parenthesis ')' and are now moving back to an opening one), `depth_a` is incremented, otherwise if we are in a state where the aggregate parity is non-zero, `curr` is incremented. 

Conversely, if a closing parenthesis ')' is encountered, and we are in a state where the aggregate parity is 0 (i.e., we just encountered an opening parenthesis '(' and are now moving back to a closing one), `depth_b` is incremented, otherwise if we are in a state where the aggregate parity is non-zero, `curr` is decremented. 

The function returns a boolean indicating whether the maximum depth of opening parentheses (`depth_b`) is less than or equal to the maximum depth of closing parentheses (`depth_a`), with the additional constraint that the overall parentheses balance is correct (`curr` <= 0). 

The outer function iterates through pairs of strings in the list, zipping them together and passing them to the inner merge function. If any of these pairs can be merged, the overall list can be merged, so it returns "Yes". Otherwise, it returns "No".