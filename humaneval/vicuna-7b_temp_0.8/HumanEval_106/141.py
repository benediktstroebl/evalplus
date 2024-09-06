
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # The list that will store the result
    result = []
    
    # Check if the current index i is even or not
    even_indices = [i for i in range(n) if i % 2 == 0]
    
    # If even_indices is not empty, then add the value of the factorial of each even index to the result
    for i in even_indices:
        result.append(i * i)
    
    # If even_indices is empty, then check if the current index i is odd or not
    odd_indices = [i for i in range(n) if i % 2 != 0]
    
    # If odd_indices is not empty, then add the sum of numbers from 1 to i to the result
    for i in odd_indices:
        result.append(i + 1)
    
    return result