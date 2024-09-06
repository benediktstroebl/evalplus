
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
    # def count_brackets(s):
    #     opening = closing = 0
    #     for letter in s:
    #         if letter == '[':
    #             opening += 1
    #         else:
    #             closing += 1
    #     return opening, closing
    #
    #
    # opening, closing = count_brackets(string)
    # print(string)
    # print(opening)
    # print(closing)
    # if opening == closing:
    #     return False
    # return True
    if string[0] == '[':
        return False
    elif string[-1] == ']':
        return False
    else:
        return True

