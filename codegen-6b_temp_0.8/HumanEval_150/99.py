
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n%2 == 0 and n != 2:
        return y
    else:
        return x

"""
A function called divisible that takes three parameters and returns
p if the first parameter is divisible by the second parameter. If it is
not, it returns q.

   Examples: 
for divisible(90, 5, 6) == 60
   for divisible(10, 10, 10) == 10
   for divisible(3, 3, 3) == 3
   for divisible(175, 15, 7) == 175

"""