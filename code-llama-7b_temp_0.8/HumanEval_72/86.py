
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

    # Create two functions, one for checking if the list is balanced, one for checking the sum of the list
    
    # Create a function for checking if the list is balanced
    def balanced(q):
        # Create a variable to store the length of the list
        num_elements = len(q)
        # Create a variable to store the length of the list
        list_length = int(num_elements/2)
        
        # Create a variable to store the first half of the list
        first_half = q[:list_length]
        # Create a variable to store the last half of the list
        last_half = q[list_length:]
        
        # Iterate through the first half of the list and check if the first value in that list is the same as the last value in the second half of the list
        for i in first_half:
            if i == last_half[-1]:
                last_half.pop(0)
            else:
                return False
        return True
    
    # Create a function for checking the sum of the list
    def sum(q):
        # Create a variable to store the sum
        total = 0
        
        # Iterate through the list and add up all of the values
        for i in q:
            total += i
            
        # Return the sum
        return total
    
    # Check if the list is balanced
    balanced_check = balanced(q)
    # Check if the sum of the list is less than or equal to the maximum weight
    sum_check = sum(q) <= w
    
    # Return True if both conditions are met
    if balanced_check and sum_check:
        return True
    # Return False otherwise
    else:
        return False
    
