```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    if max(open_tup) != max(close_tup):
        return 'No'
    return 'Yes'

def count_open(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
    return balance
```

The code utilizes two functions: `count_open`, which counts the balance of open parentheses in a given string, and `match_parens`, which takes a list of strings as input and determines if they can be concatenated to form a balanced string. 

The `match_parens` function uses `count_open` to calculate the balance of open parentheses for both input strings. It then compares the maximum balance of open parentheses in each string and returns 'No' immediately if they are unequal, indicating no way to achieve a balanced concatenation. If the max balances are equal, it returns 'Yes', suggesting a possible balanced concatenation. 

This solution is concise and adheres to the problem statement's guidelines, and the included `count_open` function helps to simplify the overall logic.