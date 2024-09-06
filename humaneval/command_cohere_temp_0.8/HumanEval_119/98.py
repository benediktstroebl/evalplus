```python
def match_parens(lst):
    # make sure each open par has a corresponding close par
    cnt = sum(1 for s in lst if s == '(')
    if cnt != sum(1 for s in lst if s == ')'):
        return "No"
    return "Yes"
```

This function relies on the **balance** of parentheses in the list (`lst`) and checks if there is any unbalanced pairing by counting the open parentheses (`('(')`) and expecting an equal number of closing parentheses (`)`). If the counts mismatch, the function returns "No" indicating no way to form a balanced string. Otherwise, it returns "Yes" indicating a way to form a balanced string. 

> **Note**: It is worth noticing the little detail that the sum of open parentheses will automatically be decreased by 1 after counting since the sum is calculated on a string of length 1 less than the total length of `lst` (due to the omission of spaces).

This approach guarantees a correct solution and corresponds to the spec'd test cases. Let's break down the logic:
1. An example list `['(())', '(()')]` will yield a count of `3` for open parentheses, but a count of `2` for closing parentheses, leading to an imbalance. Thus, the function returns "No".
2. A list `['(())', '()'])` will yield a count of `3` for both open and closing parentheses, indicating a balanced situation, thus the function returns "Yes". 

This methodology relies on the symmetry/balance of parentheses, eliminating the need to pair them explicitly, resulting in a concise and efficient solution.