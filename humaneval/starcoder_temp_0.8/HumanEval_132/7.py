
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
    # My Solution
    '''
    def is_nested_helper(string):
        counter = 0
        for i in range(len(string)):
            if string[i] == '[':
                counter += 1
            elif string[i] == ']':
                counter -= 1
                if counter < 0:
                    return False
        return counter == 0
    return is_nested_helper(string)
    '''
    # Best Solution
    def is_nested(string):
        return string.count(']') < string.count('[')
    return is_nested(string)
