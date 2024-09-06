
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

    # [['[['
    # ']]]]]][['
    # '[]]]]]]][['
    # '[][]'
    # '[]]'

    # is_nested('[[[[]][]][]]')
    # is_nested('[[[[]][]][]]')

    def is_nested(string):
        is_nested_list = []
        is_nested_count = 0
        for char in string:
            if char == '[':
                is_nested_count += 1
                is_nested_list.append(is_nested_count)
            if char == ']':
                is_nested_count -= 1

        for i in is_nested_list:
            if i > 1:
                return True
        return False

    return is_nested(string)


