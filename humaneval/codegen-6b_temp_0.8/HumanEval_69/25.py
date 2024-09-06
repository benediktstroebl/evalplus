
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # @lint_utils.typecheck
    def find(lst, f):
        '''
        return the first element whose frequency is greater than or equal to f.
        '''
        for i in lst:
            if f[i] >= i:
                return i
        return -1
    # @lint_utils.typecheck
    def freq(lst):
        '''
        return the frequency map where the key is the element and the value is the frequency of the element.
        '''
        dct = {}
        for i in lst:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        return dct
    # @lint_utils.typecheck
    def up(lst, f, k):
        '''
        update f, check if k is the first element whose frequency is greater than or equal to f.
        '''
        if k in f:
            f[k] += 1
            return True
        return False
    # @lint_utils.typecheck
    def down(lst, f, k):
        '''
        update f, check if k is the first element whose frequency is less than f. If yes, then delete k.
        '''
        if k in f:
            if f[k] == 1:
                del f[k]
            else:
                f[k] -= 1
            return True
        return False
    # @lint_utils.typecheck
    def iterate(lst, f, k):
        '''
        update f, check if k is the first element whose frequency is greater than or equal to f.
        '''
        return up(lst, f, k) or down(lst, f, k)
    f = freq(lst)
    first = find(lst, f)
    if first == -1:
        return -1
    last = lst[-1]
    while first < last:
        first = iterate(lst, f, first)
    return first