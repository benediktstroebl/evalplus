
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
    # your code here


    # def is_nested(string):
    #     stack = []

    #     for i in string:
    #         if i == '[':
    #             stack.append(i)
    #         elif i == ']':
    #             if stack[-1] == '[':
    #                 stack.pop()
    #             else:
    #                 stack.append(i)
    #     return len(stack) == 0

    # return is_nested(string)

    def is_nested(string):
        num_open = 0

        for c in string:
            if c == '[':
                num_open += 1
            else:
                if num_open == 0:
                    return False
                else:
                    num_open -= 1

        return num_open == 0

    return is_nested(string)
