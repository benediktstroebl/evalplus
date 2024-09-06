
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
    # Your code here
    
    string = string.lower()
    sublist = []
    nest_level = 0
    for char in string:
        if char == '[':
            nest_level += 1
            sublist.append(char)
        elif char == ']':
            if nest_level > 0:
                nest_level -= 1
                sublist.pop()
                if not nest_level == 0:
                    sublist.append(char)
    if len(sublist) > 0:
        return True
    else:
        return False
