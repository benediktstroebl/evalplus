
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
    string = list(string)
    nest_count = 0
    nest = []
    for i in range(len(string)):
        if string[i] == '[' and i > 0 and string[i-1] == ']':
            nest.append(string[i])
            nest_count += 1
        elif string[i] == '[' and not i > 0 or string[i-1] != ']':
            if nest_count > 0:
                nest_count -= 1
                if nest_count == 0:
                    return True
            nest.pop()
    if len(nest) > 0:
        return True
    else:
        return False

test_input = input()
result = is_nested(test_input)
