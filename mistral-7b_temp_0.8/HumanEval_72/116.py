
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



    def palindromo(q):
        if q == q[::-1]:
            return True
        else:
            return False

    if (palindromo(q) == True) and (sum(q) <= w):
        return True
    else:
        return False


    #pruebas
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3, 2, 3], 1) == False
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([3], 5) == True
    assert will_it_fly([2, 2, 2, 2, 2], 10) == False
    assert will_it_fly([3, 3], 6) == False
    assert will_it_fly([1, 1], 2) == False
    assert will_it_fly([1, 1, 1], 3) == False
    assert will_it_fly([
