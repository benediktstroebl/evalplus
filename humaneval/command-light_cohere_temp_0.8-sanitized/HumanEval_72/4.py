def will_it_fly(q, w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    '''
    balanced = True if len(q) == 2 and q[0] == q[1] else balanced
    balanced = False if len(q) > 2 and q[0] + q[1] <= w else balanced
    return balanced