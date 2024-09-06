
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

    def nested(index, count):
        if index == len(string):
            return count
        else:
            if string[index] == '[':
                return nested(index+1, count + 1)
            else:
                return nested(index+1, count - 1)

    count = 0
    return nested(0, count) > 0

