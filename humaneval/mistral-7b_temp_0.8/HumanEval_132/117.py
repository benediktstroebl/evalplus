
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

    # # Pass a string as a parameter to a function
    # string = '[][]'
    # if len(string) % 2 == 0:
    #     for i in range(0, len(string), 2):
    #         if string[i] == '[' and string[i + 1] == '[':
    #             print('Nested!')
    #         elif string[i] == '[' and string[i + 1] != '[':
    #             print('Not Nested!')
    #         elif string[i] != '[' and string[i + 1] == '[':
    #             print('Not Nested!')
    #         else:
    #             print('Nested!')
    #
    #     # Use return to pass a value back to the calling code
    #     return string

    # # Print the result
    # print(f'String contains nested brackets? {is_nested(string)}')

    string = '[]]]]]]][[[[[]'
    if string == '':
        return False
