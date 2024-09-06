
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
    # attempt one - 1
    brackets = []
    for char in string:
        if char == ']':
            if '[' in brackets:
                brackets.remove('[')
            else:
                return False
        else:
            brackets.append(char)
    return True
    
    # attempt one - 2
    if '[' not in string:
        return False
    return True if '[]' in string else False
    
    # attempt one - 3
    count = 0
    for char in string:
        if char == '[':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True if count == 0 else False
    
    # 1
    # strings = [i for i in string if i == '[' or i == ']']
    # count = 0
    # for char in strings:
    #     if char == '[':
    #         count += 1
    #     else:
    #         if count == 0:
    #             return False
    #         count -= 1
    # return True if count == 0 else False
    
    # 2
    # string = string.replace(']', '(')
    # string = string.replace('[', ')')
    # return '(' in string
    
    # 3
    # string = string.replace('[', '')
    # string = string.replace(']', '')
    # return '[]' in string
