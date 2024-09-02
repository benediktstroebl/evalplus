
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
    # Write your code here
    # This is a basic implementation, you can improve it by removing unnecessary lines of code
    nested = []
    count = 0
    for char in string:
        if char == "]":
            if len(nested) == 0:
                count += 1
            else:
                count -= 1
                nested.pop()
        elif char == "[" and len(nested) != 0:
            nested.append(count)
            count += 1
        elif char == "[":
            count += 1

    if count != 0:
        return False
    else:
        return True
    # Alternative solution, but it doesn't check if the outermost brackets are nested.
    # my_string = string.replace('[', '').replace(']', '')
    # return '[' + my_string + ']' in my_string


