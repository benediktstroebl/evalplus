
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    if not lst:
        return 'No'
    if len(lst) == 1:
        return 'Yes' if lst[0] == '(' and lst[0] == ')'" else 'No'
    for i in range(len(lst)):
        if lst[i] == '(' and lst[i+1] == ')':
            lst[i] = '('
            lst[i+1] = ')';
            if match_parens(lst[:i] + [lst[i+2]] + lst[i+2:]) == 'Yes':
                return 'Yes'
    return 'No'

inputs = [
('(', '('),
('[', '['),
(')', ')'),
(']', ']'),
('[', '['),
(')', ')'),
(']', ']'),
('(', '('),
(']', ')')
]

for i in range(len(inputs)):
    if inputs[i][0] == inputs[i][1]:
        inputs[i] = (inputs[i][0], inputs[i][1])
    else:
        inputs[i] = '(' + inputs[i][0] + ')', ')'

for i in range(len(inputs)):
    print(inputs[i], ' == ', match_parens(inputs[i+1:]))