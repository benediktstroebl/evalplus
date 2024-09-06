
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

    # FUNCTIONS
    def is_palindromic(arr):
        '''
        Check if the array is palindromic
        '''
        # validations
        if type(arr) != list:
            raise TypeError('arr must be a list.')

        # init variables
        arr_reversed = arr[::-1]

        if len(arr) == 1:
            return True

        # check if is palindromic
        for i in range(len(arr)):
            if arr[i] != arr_reversed[i]:
                return False
        return True

    # CHECK IF THE LIST IS PALINDROMIC
    if is_palindromic(q) == False:
        return False

    # CHECK IF THE SUM OF THE LIST IS LESS THAN OR EQUAL THE MAXIMUM POSSIBLE WEIGHT
    sum = 0
    for i in q:
        sum = sum + i
    if sum <= w:
        return True
    else:
        return False
