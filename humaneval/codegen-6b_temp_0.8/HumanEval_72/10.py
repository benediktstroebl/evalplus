
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
    def is_palidromic(l):
        return l == l[::-1]
    def sum_list(l):
        sum = 0
        for i in l:
            sum += i
        return sum
    def compare(l):
        for i in l:
            if sum_list(i) > w:
                return False
        return True
    def return_palidromic_list(l):
        return l + l
    def make_list(f,l):
        l1 = []
        for i in l:
            l1.append(f(i))
        return l1
    def return_list(q,w):
        r = q
        if compare(r):
            return r
        r = make_list(r,r)
        r = make_list(return_palidromic_list,r)
        return r
    return return_list(q,w)
will_it_fly([3, 2, 3], 1)
will_it_fly([1, 2], 5)
will_it_fly([3, 2, 3], 9)
will_it_fly([2, 4, 6], 1)
will_it_fly([1, 1, 1, 1, 1], 10)
will_it_fly([3, 2, 3], 1)
will_it_fly([3, 2, 3], 9)
will_it_fly([3, 2, 3], 10)
will_it_fly([3, 2, 3], 11)
will_it_fly([3, 2, 3], 12)
will_it_fly([3, 2, 3], 13)
will_it_fly([3, 2, 3], 14)
will_it_fly([3, 2, 3], 15)
will_it_fly([3, 2, 3], 16)
will_it_fly([3, 2, 3], 17)
will_it_fly([3, 2, 3], 18)
will_it_fly([3, 2, 3], 19)
will_it_fly([3, 2, 3], 20)
will_it_fly([3, 2, 3], 21)
will_it_fly