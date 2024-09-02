
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    
    # create empty list called 'list1'
    list1 = []

    # create for loop to iterate through all items in n
    for i in range(1,n+1):
        
        # create if statement to check if i is even
        if i % 2 == 0:
            list1.append(i)
        else:
            
            # create for loop to iterate through all items in i
            for j in range(1, i+1):
                
                # create if statement to check if j is even
                if j % 2 == 0:
                    continue
                else:
                    list1.append(sum(range(1, i+1)))

    return list1
