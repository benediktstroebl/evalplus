
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # your code here
    # a list of 0's of size n
    my_list = []
    for i in range(n):
        if i%2 == 0:
            # factorial of i
            my_list.append(i*(i-1)*(i-2)*(i-3)*(i-4)*(i-5))
        else:
            # sum of numbers from 1 to i
            my_list.append(i*(i-1)/2)
    return my_list
