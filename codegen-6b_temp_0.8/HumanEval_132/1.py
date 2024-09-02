
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
    def is_nested_helper(string, start, end):

        def has_bracket(i):
            return string[i] in ['[',']']

        def num_brackets(i):
            count = 1
            i += 1
            while(i < len(string) and not has_bracket(i)):
                if has_bracket(i):
                    count += 1
                i += 1
            return count

        if start == end:
            return True
        if end == len(string):
            return False
        if has_bracket(start):
            return is_nested_helper(string, start + 1, end)
        if start + 1 == end:
            if num_brackets(start) > num_brackets(end):
                return is_nested_helper(string, start, end - 1)
            else:
                return is_nested_helper(string, start + 1, end)
        return is_nested_helper(string, start + 1, end) or is_nested_helper(string, start, end - 1)

    return is_nested_helper(string, 0, len(string))
