```python
def match_parens(lst):
    opens = {'(':0, '':1}
    closes = {')':0, '':1}
    sum_par = sum(opens.get(x,0) for x in lst[0]) - \
              sum(closes.get(x,0) for x in lst[1])
    return 'Yes' if sum_par == 0 else 'No'
```

The function iterates through the provided list of strings, specifically counting the open and closed parentheses through a dictionary utilization. The cumulative count of open parentheses from the first string and closed parentheses from the second string is then differentiated to determine if a balanced concatenation is possible. If the differential is zero, the function returns "Yes"; otherwise, it returns "No". 

This approach ensures correctness in determining the balance of parentheses and provides the desired output based on the provided criteria.