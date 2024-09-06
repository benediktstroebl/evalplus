
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
    # chosen_brackets = set()
    # opened_brackets = set()
    # matched = True
    # for bracket in string:
    #     if bracket in bracket_pairs:
    #         if bracket in string[string.index(bracket):]:
    #             continue
    #         else:
    #             matched = False
    #             break
    #     elif bracket in closing_brackets:
    #         if bracket in string[string.index(bracket):]:
    #             opened_brackets.add(bracket)
    #         else:
    #             matched = False
    #             break
    #     elif bracket in opening_brackets:
    #         if bracket in string[string.index(bracket):]:
    #             chosen_brackets.add(bracket)
    #         else:
    #             matched = False
    #             break
    # if matched == True:
    #     return True
    # else:
    #     return False

    def nested_brackets(string):
        if not string:
            return 0
        stack = []
        for bracket in string:
            if bracket in closing_brackets:
                if not stack:
                    return 0
                if closing_brackets[bracket] != stack[-1]:
                    return 0
                else:
                    stack.pop()
            elif bracket in opening_brackets:
                stack.append(bracket)
        return 1 if len(stack) == 0 else 0

    opening_brackets = set("([{")
    closing_brackets = set(")]}")
    bracket_pairs = {"(": ")", "{": "}", "[": "]"}

    return nested_brackets(string) > 0
