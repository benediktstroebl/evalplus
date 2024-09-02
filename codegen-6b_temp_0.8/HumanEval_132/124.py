
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
    brackets = [character for character in string]
    valid = 0
    opening = 0
    for i in range(len(brackets)):
        if brackets[i] == '[':
            # valid += 1
            opening += 1
        elif brackets[i] == ']':
            # if valid == 0:
            #     return False
            opening -= 1
            if opening < 0:
                return False
            # valid -= 1
    if opening > 0:
        # return False
        return True
    else:
        return False