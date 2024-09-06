
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
    nested_indices = []
    for index in range(len(string)):
        if string[index] == '[' and string[index+1] == '[' and string[index+2] == '[':
            nested_indices.append(index+2)
            while nested_indices and nested_indices[-1] == string[nested_indices[-2]-1]:
                nested_indices.pop()
            if nested_indices:
                nested_indices.pop()
                if nested_indices[-1] == string[nested_indices[-2]-1]:
                    nested_indices.pop()
    return len(nested_indices) > 0
