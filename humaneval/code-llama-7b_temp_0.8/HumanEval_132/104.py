
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
    # Create an array of the brackets. 
    brackets_array = [string[i] for i in range(len(string))]
    # Create a new array with nested brackets.
    nested_brackets = []
    for i in range(len(brackets_array)):
        if brackets_array[i] == '[' and brackets_array[i + 1] == '[':
            nested_brackets.append('[[')
        else:
            nested_brackets.append(brackets_array[i])
    # Check if the length of the new array is more than one.
    return len(nested_brackets) > 1

