
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # The list to store the answer
    answer = [1]
    
    # The loop to find the factorial of odd numbers
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            answer.append(i * i)
        else:
            answer.append(i)
    
    # The loop to find the sum of numbers from 1 to i if i is odd
    for i in range(n-1, -1, -1):
        if i % 2 != 0:
            answer.append(i + answer[i])
    
    return answer
