
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    '''
    
    # Write code here
    # Inputs: list (list of numbers)
    # Output: int
    
    # Ignore negative numbers
    # Ignore non integers
    # Squares of odd numbers (including 0)
    
    # Convert list to string
    # Convert string to list
    # For each item in list, convert to int
    # Check if int is odd, convert to square
    # Add squares to total
    
    # Return total
    
    list_to_str = str(lst)
    list_to_str = list(list_to_str)
    list_to_int = []
    for i in list_to_str:
        list_to_int.append(int(i))
    
    total = 0
    for i in list_to_int:
        if i % 2 == 1:
            i = i ** 2
            total += i
    
    return total
    
