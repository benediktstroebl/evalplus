
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
    lst = []
    for n in string:
        if n == '[':
            lst.append(n)
        elif n == ']':
            if len(lst) == 0:
                return False
            lst.pop()
    return len(lst) == 0
                
assert is_nested('[[]]') == True
assert is_nested('[]]]]][[[[[]') == False
assert is_nested('[][]') == False
assert is_nested('[]') == False
assert is_nested('[[][]]') == True
assert is_nested('[[]][[') == True
assert is_nested('[][[]]') == False


from itertools import combinations