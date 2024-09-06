```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if open_tup == close_tup else "No"

def count_parens(s):
    return len(s) // 2
```
The function `match_parens` takes in a list of two strings, both containing only open or close parentheses. It employs the `count_parens` function to count the number of open parentheses in each string. These counts are then compared through tuples. If the counts are equal, the two strings can be concatenated in some order to yield a balanced parentheses string, indicating "Yes." Otherwise, indicating an imbalance, the result is "No". 

This solution has a time complexity of O(n log n), where n is the number of characters in the strings, owing to the `count_parens` function.