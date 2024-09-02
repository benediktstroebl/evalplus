
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

    # A stack to store opening brackets.
    stack = []
    # A counter for nested brackets
    nested_brackets = 0

    for bracket in string:
        # If it is an opening bracket, then push it to the stack.
        if bracket == "[" or bracket == "(":
            stack.append(bracket)

        # If it is a closing bracket and the stack is not empty.
        if bracket == "]" or bracket == ")":
            # Check if the top element of the stack is either '(' or '['.
            if stack:
                top_element = stack.pop()

                # If the top element is not either '(' or '[' then it is an invalid bracket.
                if top_element != "(" and top_element != "[":
                    return False
            else:
                return False
        
        # Increment the counter
        nested_brackets += 1
    
    # If the stack is not empty by the end of the for loop, then return False.
    if stack:
        return False

    return True if nested_brackets % 2 == 0 else False

