
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
    def is_palindromic(l):
        s = ''.join(str(e) for e in l)
        if s == s[::-1]:
            return True
        else:
            return False

    def sum_less_max(l):
        sum = 0
        for x in l:
            sum = sum + x
        return sum
    
    def flat_list(l):
        fl = []
        for elem in l:
            if type(elem) == list:
                fl.extend(flat_list(elem))
            else:
                fl.append(elem)
        return fl
    
    a = flat_list(q)
    b = sum_less_max(a)
    if is_palindromic(a) == True and b <= w:
        return True 
    else:
        return False
