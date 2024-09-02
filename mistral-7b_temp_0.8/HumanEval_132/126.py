
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
    #   Решение через рекурсию
    def is_nested(str):
        if str.count('[') == str.count(']'):
            return True
        elif str[0] == '[' and str[-1] == ']':
            return True
        else:
            return is_nested(str[1:])



    return is_nested(string)
    #   Решение без рекурсии
    # def is_nested(str):
    #     start_count, end_count = 0, 0
    #     for ch in str:
    #         if ch == '[':
    #             start_count += 1
    #         elif ch == ']':
    #             end_count += 1
    #         if end_count > start_count:
    #             return False
    #     return True

    # return is_nested(string)
