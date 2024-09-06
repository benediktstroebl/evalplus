```python
def separate_paren_groups(s: str) -> List[str]:
    result = []
    opening_p = '([{"]
    closing_p = '})'
    while opening_p in s:
        after_closing = s.find(closing_p)
        result.append(after_closing)
        s = s.replace(opening_p, ' ' + after_closing + closing_p)
    return result

tests = []
tests.add('([r'\n( )\n(( ))\n(( ))()', ['n', '(', ')'])])
tests.add('([r'\n( ) (( )))', ['()'])] * 2)
tests.add('([r'\n( )( )()\n(( ))()', ['()', '()()'])] * 2)
tests = [test[0] for test in tests]
print(f"Test results: {', ', '.join(map(str, tests))))
``` 
This function, named `separate_paren_groups`, takes a string `s` as input and splits it into individual groups of parentheses. It then returns a each group as a separate string.