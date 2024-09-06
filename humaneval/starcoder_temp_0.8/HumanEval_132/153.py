
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
    # Your code here
    open_brackets = ['[', '(', '{']
    close_brackets = [']', ')', '}']
    open_index = []
    close_index = []

    for i in range(len(string)):
        if string[i] in open_brackets:
            open_index.append(i)
        elif string[i] in close_brackets:
            close_index.append(i)
    
    if len(open_index)!= len(close_index):
        return False
    else:
        for i in range(len(open_index)):
            if open_index[i] > close_index[i]:
                return False
        return True

