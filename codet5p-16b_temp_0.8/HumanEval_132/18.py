
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

    is_nested = False
    if string == None:
        return is_nested
    if len(string) == 1:
        return False
    if len(string) % 2 == 1:
        return False

    list_ = []
    string_temp = ""
    for char in string:
        if char == '[' or char == '{':
            list_.append(char)
            string_temp += char
        else:
            if char == ']' or char == '}':
                if len(list_) > 0:
                    if char == ']' and list_[-1] == '[':
                        string_temp += char
                        list_.pop()
                    if char == '}' and list_[-1] == '{':
                        string_temp += char
                        list_.pop()
                else:
                    return False
    if list_:
        return False
    else:
        return True
