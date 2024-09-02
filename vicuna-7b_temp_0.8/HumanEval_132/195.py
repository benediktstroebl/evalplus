
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
    def helper(s):
        stack = []
        last_index = 0
        for i in range(1, len(s)):
            if s[i:i+1] == "[" or s[i:i+1] == "]" or s[i:i+1] == "]":
                if s[last_index-1] == "[" and s[last_index] == "]":
                    stack.append(s[last_index-1])
                    last_index -= 2
                elif s[last_index-1] == "]" and s[last_index] == "[":
                    stack.append(s[last_index-1])
                    last_index -= 2
                else:
                    if stack:
                        if s[last_index-1] == "[" and s[last_index] == "]":
                            if stack[-1] == "[" and s[last_index-2] == "]":
                                stack.pop()
                                last_index -= 2
                            else:
                                stack.pop()
                        else:
                            if s[last_index-1] == "[" and s[last_index] == "]":
                                return True
                            else:
                                return False
            else:
                last_index = i
        return False
    return helper(string)
