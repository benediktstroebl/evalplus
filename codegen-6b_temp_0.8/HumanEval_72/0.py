
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
    
    def _is_palindromic(lst):
        return lst == lst[::-1]

    def _balance_sum(lst):
        return sum(map(int, lst))
    
    def _is_low_enough(w, balance):
        return balance < w

    def _can_fly(q, w, balance):
        return (_is_palindromic(q) and _is_low_enough(w, balance) )

    def _fly(q,w,balance):
        return _can_fly(q,w,balance) and _balance_sum(q) <= balance

    return _fly(q,w, False)

assert will_it_fly([1,2], 5) == False
assert will_it_fly([3, 2, 3], 1) == False
assert will_it_fly([3, 2, 3], 9) == True
assert will_it_fly([3], 5) == True
assert will_it_fly([1,2,3,4,5,6,7,8,9,10], 100) == True