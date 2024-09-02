
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
    #1
    #x=q
    #y=w
    #return q.count(q[::-1])<=1 and x+y<=w

    #2
    #x=q
    #y=w
    #return q[::-1]==q and x+y<=w

    #3
    #x=q
    #y=w
    #return q==q[::-1] and x+y<=w

    #4
    #x=q
    #y=w
    #return q[::-1]==x and x+y<=w

    #5
    #x=q
    #y=w
    #return x[::-1]==x and x+y<=w

    #6
    #x=q
    #y=w
    #return len(q)==q[::-1] and x+y<=w

    #7
    #x=q
    #y=w
    #return len(q)==len(q[::-1]) and x+y<=w
