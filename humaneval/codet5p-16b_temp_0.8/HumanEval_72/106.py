
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

    
    #The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.
    
    #Function that returns True if the object q will fly, and False otherwise.
    def will_it_fly(q,w):
        
        #Checks if q is balanced, which is a palindromic list.
        def check(p):
            
            #Creates a new list with the elements of p in reverse order.
            p = list(p)[::-1]
            
            #The sum of the elements of the list p is the sum of its elements in reverse order.
            return sum(p) == sum(q)
        
        #Checks if the sum of the elements of the list p is less than or equal the maximum possible weight w.
        return sum(q) <= w and check(q)
    
    #Returns True if the object q will fly, and False otherwise.
    return will_it_fly(q,w)

    
