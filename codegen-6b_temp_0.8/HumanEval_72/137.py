
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
    def sum_and_len(l):
        sum_ = 0
        for i in l:
            sum_ += i
        return (sum_, len(l))
    
    def palindrom(l):
        for i, j in zip(l, l[::-1]):
            if i != j:
                return False
        return True
    
    def test(l, w):
        if palindrom(l) is False:
            return False
        sum_, len_ = sum_and_len(l)
        return sum_ <= w
    
    return test(q, w)
