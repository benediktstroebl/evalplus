
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # As a working solution, I first set up a list of the lengths, then
    # I take zip with my own list of the length 1st list, then I use sum
    # to add up the 1st and 2nd lengths, which gives me a list of 2 sums,
    # then I use the list of 2 sums to create a list that I use to check
    # if the sum of any pair of numbers is greater than the third. If it 
    # is, I return the sum of the 2 sums divided by 2, otherwise, return -1
    
    # All of these lines are missing the return statement, but I'm getting
    # a syntax error when trying to run the code
    l = [a, b, c]
    return [round(sum(i) / 2, 2) for i in zip(l, l[1:]) if sum(i) > sum(l)][0] if all(i > 0 for i in l) and a + b > c else -1
