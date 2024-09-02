
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
    
    if '[' in string and ']' in string:
        nested_brackets = []
        nested_indexes = []
        for index, char in enumerate(string):
            if char == '[':
                nested_brackets.append(char)
                nested_indexes.append(index)
            elif char == ']':
                if nested_brackets:
                    nested_brackets.pop()
                else:
                    return False
        
        return is_nested(string[nested_indexes[0]+1:nested_indexes[-1]])
    else:
        return
