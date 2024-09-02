
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
    def stack():
        opening = []
        closing = []
        index = 0
        while index < len(string):
            if string[index] == '[':
                opening.append(index)
            else:
                closing.append(index)
            index += 1
        return opening, closing

    opening, closing = stack()
    if len(opening) == 0 or len(closing) == 0:
        return False
    if opening[-1] > closing[0]:
        return True
    else:
        return False
        


