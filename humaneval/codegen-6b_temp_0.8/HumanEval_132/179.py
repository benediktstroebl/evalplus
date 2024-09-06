
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
    # your code here
    bool = True
    stack = []
    for i in string:
        if i == '[' and bool:
            stack.append(i)
        elif i == ']' and not bool:
            stack.pop()
        else:
            if not bool:
                bool = True
            else:
                bool = False
    return bool
