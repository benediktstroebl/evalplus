
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]

    first_element = 1
    second_element = 1
    i = 2
    while i <= n:
        second_element = second_element * i
        i = i + 1

    result = [first_element]
    while second_element!= 1:
        result.append(second_element)
        second_element = second_element // first_element
        first_element = first_element + 1

    return
