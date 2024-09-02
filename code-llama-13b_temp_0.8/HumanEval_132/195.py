
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
    # def check(list_nested):
    #     return list_nested.count('[') == list_nested.count(']')
    def check(string):
        return string.count('[') == string.count(']')
    list_nested = []
    for i in range(len(string)):
        if string[i] == '[':
            list_nested.append(string[i])
        else:
            if len(list_nested) > 0 and check(list_nested):
                return True
            list_nested.pop()
    return check(list_nested) and len(list_nested) == 0

