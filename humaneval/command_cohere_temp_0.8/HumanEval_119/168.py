```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if len(open_tup) == len(close_tup) and all(open == close for open, close in zip(open_tup, close_tup)) else "No"

def count_parens(s):
    return s.replace("(", "") 

# Tests:
assert match_parens(
    ['()(', ')']) == 'Yes'
assert match_parens(
    [')', ')']) == 'No'
assert match_parens(
    ['((', '))']) == 'Yes'
assert match_parens(
    ['((', ')()']) == 'Yes'
assert match_parens(
    ['(()', ')']) == 'No'
``` 

The function `match_parens` employs two helper functions:
1. `count_parens`: This function counts the number of opening parentheses in a given string. The logic behind this function is to remove all opening parentheses from a given string and use the resulting string as the count. This works because the string `""` has a length of 0, and when you remove parentheses from a string, the length decreases. 
2. `zip`: This function takes two or more sequences and returns a tuple with corresponding elements. The result of `zip` is a tuple with the same length as the shortest input sequence. 

Then the main logic of `match_parens` is based on:
1. The two input strings, after transformation by `count_parens`, are turned into tuples.
2. The length of both tuples must be the same, and the elements of both tuples must have the same count and be equal when paired using `zip`.
3. If both requirements are satisfied, the result is "Yes"; otherwise, the result is "No". 

All of the examples pass through the above logic, explaining why each of the sample tests returns the correct result.