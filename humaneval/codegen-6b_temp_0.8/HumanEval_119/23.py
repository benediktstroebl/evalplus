
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
    def helper(s, visited, is_left, nums, num_left, memo):
        if s in visited:
            return visited[s]

        if s == '':
            visited[s] = True
            return True

        if s == '(':
            return False

        if s == ')':
            return False

        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == num_left and right == num_left:
                nums.add(s)
                return

            if left < num_left and right < num_left:
                continue

            if left > right:
                helper(s[:i] + '(' + s[i:], visited, True, nums, left, memo)
                helper(s[:i], visited, False, nums, right, memo)
            else:
                helper(s[:i] + ')' + s[i:], visited, False, nums, left, memo)
                helper(s[:i], visited, True, nums, right, memo)

        if len(s) == num_left:
            nums.add(s)
            return

        if s[0] == ')':
            visited[s] = False
            return False

        visited[s] = helper(s[1:], visited, True, nums, num_left, memo)

    nums = set()
    memo = {}
    helper('', {}, True, nums, 0, memo)
    return 'Yes' if nums else 'No'

