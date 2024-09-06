
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
    
    def get_sum(lst):
        result = 0
        for elem in lst:
            result += elem
        return result
    
    def is_balanced(lst):
        for i in range(len(lst)/2):
            if lst[i] != lst[-i-1]:
                return False
        return True
    
    def is_valid(lst,w):
        if is_balanced([elem for elem in lst if elem > 0]) and get_sum(lst) <= w:
            return True
        return False
    
    return is_valid(q,w) and is_balanced(q)