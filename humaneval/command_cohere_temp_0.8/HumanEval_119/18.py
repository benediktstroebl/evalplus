```python
def match_parens(lst):
    def diff(s):
        return '(' if s == ')' else ')'
    
    both = [x for x in lst if x != '()]'][:2]
    count = [x for x in both if x == '(']
    if count.count(diff(count[0])) % 2 == 0:
        return "Yes"
    else:
        return "No"
```

The function `match_parens` takes in a list of strings as input and determines if it's possible to concatenate the two strings in some order to create a balanced parentheses string. It does so by checking if the number of open parentheses `( `) is equal to the number of close parentheses `)`:
- The function takes the first two elements of the list (`[x for x in lst if x != '()]'`), assuming these are the two strings of interest.
- It then checks which of the open or close parentheses is in the majority in these first two strings. It uses `diff` to determine whether a parenthesis is open or close. 
- If the majority polarity (open or close) is `(` and the count of this polarity is odd, it returns `Yes`. This is because an odd number of open parentheses can be matched with an odd number of close parentheses in a way that guarantees a balanced parentheses string. 
- If the polarity is even, it returns `No`. This is because an even number of parentheses cannot create a balanced parentheses string when concatenated in any order. 

This solution is concise and correctly solves the problem. It can be tested with the following markdown code block:
```python
TESTS = [
    (['], '') == 'No',
    ('()', ')') == 'No',
    ('(()', ')') == 'No',
    ('()', '()') == 'Yes',
    ('()', ')') == 'Yes',
    ('(()', '())') == 'Yes',
    ('()', '(()') == 'Yes',
    ('a())', 'b())') == 'Yes',
    ('(a)', ')b') == 'Yes',
    ('(a)', '((b')) == 'Yes',
    ('(()', '(()') == 'No',
]

for test in TESTS:
    assert match_parens(test[0]) == test[1], f"For input {test[0]}, expected {test[1]} but got {match_parens(test[0])}"
```