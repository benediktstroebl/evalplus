
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
    # BRACKET MATCHING
    # TC: O(n) | SC: O(1)
    OPENING_BRACKETS = ["[", "("]
    CLOSING_BRACKETS = ["]", ")"]
    stack = []
    for letter in string:
        if letter in OPENING_BRACKETS:
            stack.append(letter)
        elif letter in CLOSING_BRACKETS:
            try:
                if letter == "]" and stack[-1] == "[":
                    stack.pop()
                if letter == ")" and stack[-1] == "(":
                    stack.pop()
            except IndexError:
                return False
    return len(stack) != 0
