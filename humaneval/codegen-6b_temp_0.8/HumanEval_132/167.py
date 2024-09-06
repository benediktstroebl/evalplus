
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    string = iter(string)
    open = next(string, None)
    unpaired = []
    if open is not None:
        unpaired.append(open)

    for item in string:
        if item == '[' or item =='{' or item == '(' or item == '<':
            unpaired.append(item)
        elif item == ']' or item == '}' or item == ')' or item == '>':
            p = unpaired.pop()
            if not is_nested(p, item):
                return False
        elif item == ']' or item == '}' or item == ')' or item == '>' or item is None:
            return False
    return unpaired == []
