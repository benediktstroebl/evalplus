
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
    #My solution
    #pattern = r'\[([^\[\]]*)\]'
    #result = re.findall(pattern, string)

    #if len(result) == 0:
    #    return False
    #else:
    #    for i in result:
    #        if '[' in i or ']' in i:
    #            return True
    #return False

    #Another solution
    start = 0
    count = 0

    for i in string:
        if i == '[':
            count += 1
        elif i == ']':
            if count > 0:
                count -= 1
            else:
                return True

    return False if count == 0 else True
