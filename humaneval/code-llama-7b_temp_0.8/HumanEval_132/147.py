
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
    # My solution
    # return string.count("][") > 0

    # My solution
    # str_as_list = list(string)
    # count = 0
    # for i in range(len(str_as_list)):
    #     if str_as_list[i] == "[" and str_as_list[i+1] == "]":
    #         count += 1
    # return count > 0

    # List comprehension (not as concise)
    # return True if [str_as_list.pop(str_as_list.index("]")) for _ in range(len([str_as_list.pop(str_as_list.index("[")) for _ in range(len([str_as_list.pop(str_as_list.index("]")) for _ in range(len([str_as_list.pop(str_as_list.index("[") for _ in range(len(str_as_list))]))))])))) else False

    # Solution from Codewars
    return bool([i for i, j in zip(string, string[1:] + ']') if i + j == '[]'])
