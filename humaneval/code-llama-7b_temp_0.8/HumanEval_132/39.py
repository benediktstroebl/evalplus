
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
    # string = "[]]]]]]][[[[[]"
    # l = 0
    # r = 0
    # result = 0
    # for i in string:
    #     if i == '[':
    #         l += 1
    #     elif i == ']':
    #         r += 1
    #     if l == r:
    #         result = 1
    # return result
    #
    if not (string):
        return False

    stack = []
    is_nesting = False
    for letter in string:
        if letter == '[':
            stack.append(letter)
        else:
            if stack:
                stack.pop()
            else:
                return False

        if len(stack) >= 1:
            is_nesting = True

    return is_nesting

