
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
    nest_count = 0
    current_nesting = []
    for char in string:
        if char == '[' or char == ']':
            nest_count += 1
            current_nesting.append(char)
        elif char == ']':
            if current_nesting:
                if any(char == '[' for char in current_nesting[-1:]):
                    nest_count -= 1
                    current_nesting.pop()
                else:
                    nest_count -= 1
            else:
                return False
        elif nest_count == 0 and not current_nesting:
            return True
    return False
