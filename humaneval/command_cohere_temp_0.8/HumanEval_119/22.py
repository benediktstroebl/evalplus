```python
def match_parens(lst):
    cnt_open = 0
    for el in lst:
        if el == '(':
            cnt_open += 1
        else:
            cnt_open -= 1
        if cnt_open < 0:
            return "No"
    if cnt_open == 0:
        return "Yes"
    else:
        return "No"
```
This approach simply maintains a count of open parentheses and checks at the end if this count is zero, it's yes if all good else no. 
The code is self-contained and can be run directly to test it. 
It also handles the edge cases like '()' , '(((' correctly. 
If the list contains only a single string like ['('], it returns 'No' since the input is not well formed. Anecdote: This problem and its solution are notorious for being very easy for humans but quite tricky for automated tests. This is a very common question in coding interviews, and there are many different ways to solve it.