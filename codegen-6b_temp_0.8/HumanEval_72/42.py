
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
    def is_balanced(ll):
        length = len(ll)
        for i, n in enumerate(ll):
            if n % 2 == 1:
                length = i
                break
        return length == 0 or length % 2 == 0

    def sum_of_list(ll):
        length = len(ll)
        sum_l = 0
        for i, n in enumerate(ll):
            sum_l += n
            if i+1 < length:
                sum_l += ll[i+1]
        return sum_l

    if is_balanced(q) and sum_of_list(q) <= w:
        return True
    else:
        return False
