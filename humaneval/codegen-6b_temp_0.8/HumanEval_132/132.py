
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
    # can use a stack to keep track of the bracket sequence
    stack=[]

    # loop through the string
    for char in string:
        if char == '[' or char == '(' or char == '{':
            stack.append(char)
            print('stack:{}'.format(stack))
        elif char == ']' or char == ')' or char == '}':
            # check that the stack is not empty
            if len(stack) == 0:
                stack.append(char)
                # could have used a stack
                #return False
            elif (char == ']' and stack.pop() != '[') or (char == ')' and stack.pop() != '(') or (char == '}' and stack.pop() != '{'):
                stack.append(char)
                # return False
            else:
                stack.append(char)
                # check for the subsequence
                # in a nested list
                # if len(stack) > 0:
                #     return True
                # else:
                #     return False

    if len(stack) == 0:
        return True
    else:
        return False
