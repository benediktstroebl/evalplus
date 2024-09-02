
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
    if isinstance(q, list):
        if isinstance(w, int):
            if sum(q) <= w:
                for i in range(len(q)):
                    if isinstance(q[i], int):
                        q[i] += q[len(q)-1-i]
                    elif isinstance(q[i], str):
                        q[i] += q[len(q)-1-i]
                if is_palindrome(q) == True:
                    return True
    if isinstance(q, str):
        if isinstance(w, int):
            if len(q) <= w:
                return True
    if isinstance(q, int):
        if isinstance(w, int):
            if len(str(q)) <= w:
                return True
    return False
         
