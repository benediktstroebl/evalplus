
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
    def nest(string):
        nesting = []
        current_nesting = []
        for i in range(len(string)):
            if string[i] == '[' and current_nesting[-1] != ']':
                nesting.append(current_nesting)
                current_nesting = ['[', string[i]]
            elif string[i] == ']' and nesting:
                current_nesting[-1] = ']' + current_nesting[-1]
                nesting.pop()
            elif string[i] == ']':
                current_nesting.append(']')
            else:
                current_nesting.append(string[i])
        return nesting
    
    return nest(string)
