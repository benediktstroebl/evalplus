
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    
    n = int(n)
    if n == 0: return [1]
    elif n == 1: return [1, 1]
    else:
        # n>1 so we need to create a list of size n
        out = [1] * n
        
        # the index of the last n-1 elements
        last = n-1
        
        # the index of the last n elements
        last2 = n
        
        # the index of the last n elements
        last3 = n
        
        # The factorial of the last n-1 elements
        # one by one, we need to get a list of size n
        # and we will multiply them.
        while last > 1:
            # multiply the m elements with the elements
            # from 0 to n-1.
            for i in range(last):
                out[i] *= i
                
            # increase the size of the list by one element
            last -= 1
            
            # sort the elements of the list out
            out.sort()
            
            # we will carry out the same operation for
            # the factorial of the next n-1 elements
            while last2 > 1:
                for i in range(last2):
                    out[i] *= i
                last2 -= 1
                out.sort()
            
            # we will carry out the same opetion for the
            # factorial of the next n elements
            while last3 > 1:
                for i in range(last3):
                    out[i] *= i
                last3 -= 1
                out.sort()
            
        return out
    
