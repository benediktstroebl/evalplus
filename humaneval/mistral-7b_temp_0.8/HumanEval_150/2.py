
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # TO DO: Write your code below this line.
    n=int(input())
    if n%2==0:
        print(y)
    else:
        print(x)

    # TO DO: Write your code above this line.

