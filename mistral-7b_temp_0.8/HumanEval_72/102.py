
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
    # 1. Define a function called will_it_fly.
    # 2. The function should take in 2 arguments.
    # 3. The first argument is a list called q.
    # 4. The second argument is an integer called w.
    # 5. The function should return True if the list q is balanced and its sum is less than or equal to the maximum weight w.
    # 6. The function should return False if the list q is unbalanced or its sum is greater than the maximum weight w.
    # 7. Use a for loop to check if the list q is balanced.
    # 8. Use a while loop to check if the sum of the elements in the list q is less than or equal to the maximum weight w.
    # 9. If the list q is balanced and its sum is less than or equal to the maximum weight w, return True.
    # 10. If the list q is unbalanced or its sum is greater than the maximum weight w, return False.

    # 1. Define a function called will_it_fly.
    def will_it_fly
