
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
    string = str(string)
    new_string = []
    for i in string:
        if i == '[':
            new_string.append(i)
        elif i == ']':
            try:
                if new_string[len(new_string)-1] == '[':
                    new_string.pop(len(new_string)-1)
                else:
                    new_string.append(i)
            except:
                new_string.append(i)
    if len(new_string) == 0:
        return False
    else:
        return True

