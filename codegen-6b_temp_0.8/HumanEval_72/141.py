
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
    def is_palindrome(arr):
        return arr[::-1] == arr

    def check_weight(arr):
        return True if sum(arr) <= w else False

    def is_balanced(arr, level):
        if level == len(arr):
            return True
        else:
            return is_balanced(arr[1:], level + 1) if arr[0] > 0 else is_balanced(arr[1:], level + 1)

    return is_balanced(q, 0) and check_weight(q) and is_palindrome(q)
