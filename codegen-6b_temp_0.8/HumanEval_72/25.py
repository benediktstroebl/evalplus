
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    def bal(lst):
        length = len(lst)
        i = 0
        j = length - 1
        while i < j:
            if lst[i] == lst[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def sum_(lst):
        a = 0
        for i in lst:
            a += i
        return a

    if bal(q) and sum_(q) <= w:
        return True
    return False


