
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    def _inner():
        '''
        The inner function calls itself to check if there is a match. In the
        end of the while loop, the two pairs of parentheses are popped from
        the stack, and the count of remaining parentheses increments. If the
        count is not at zero, there is no way to make this string good.
        '''
        if not lst:
            return True

        l = len(lst)
        if l % 2 != 0:
            return False

        stack = []
        for i in range(l):
            if lst[i] == '(':
                stack.append(lst[i])
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0
    # This is the main function to check if there is a match.
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] == '(' and lst[right] == ')':
            lst[left], lst[right] = '', ''
            left += 1
            right -= 1
        elif lst[left] == ')':
            left += 1
        elif lst[right] == '(':
            right -= 1
        else:
            lst[left], lst[right] = '', ''
            left += 1
            right -= 1
    return 'Yes' if _inner() else 'No'

