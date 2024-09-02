
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
    def is_palindrome(lst): #this is a helper function to check if lst is a palindrome
        return lst == lst[::-1]
    
    def is_possible_max_weight(q,w):
        '''
        this is a helper function to check if the sum of elements is less than or equal to the maximum possible weight w.
        '''
        return sum(q) <= max(w, max_weight)
    
    def helper(q,w,left,right,memo):
        '''
        this is a helper function to recursively solve the problem.
        '''
        if left>right:
            return True
        if (left,right) in memo:
            return memo[(left,right)]
        if is_palindrome(q[left:right+1]):
            if is_possible_max_weight(q[left:right+1],w):
                memo[(left,right)] = True
                return True
        memo[(left,right)] = False
        return False
    
    max_weight = max(w, sum(q))
    memo = {}
    
    return helper(q,w,0,len(q)-1,memo)
