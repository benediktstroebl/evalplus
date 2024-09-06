
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
    def is_matched(expression):
        '''
        Evaluate if all brackets in the expression are matched
        '''
        # Return False if the expression is empty or contains only
        # one type of bracket.
        if len(expression) <= 1:
            return False
        # If the first character is a closing bracket then the expression
        # cannot be matched.
        if expression[0] == ']':
            return False
        # Count the number of opening and closing brackets.
        opens = expression.count('[')
        closes = expression.count(']')
        # Return False if the number of opens and closes brackets is uneven
        # or if more closes than opens.
        if opens % 2 != closes % 2 or closes > opens:
            return False
        # Remove the last element from the expression,
        # this will be the first element in the sub-expression.
        expression = expression[:-1]
        # Loop through the expression and evaluate each sub-expression
        # If a sub-expression is matched then continue to evaluate the next
        # sub-expression.
        while expression.count('[') > 0:
            sub_exp = ''
            temp = ''
            # The sub-expression will start with the first opening bracket.
            sub_exp += '['
            # Loop through the remaining characters in the expression.
            for char in expression:
                # Append each character to the sub-expression unless a closing
                # bracket is encountered.
                if char != ']':
                    sub_exp += char
                # If a closing bracket is encountered and the number of closing
                # brackets in the sub-expression is equal to the number of opening
                # brackets, evaluate the sub-expression.
                if char == ']' and sub_exp.count('[') == sub_exp.count(']'):
                    if is_matched(sub_exp):
                        # If the sub-expression is matched then continue to evaluate
                        # the remaining sub-expressions.
                        continue
                    # If the sub-expression is unmatched then return False
                    else:
                        return False
                # If a closing bracket is encountered and the
