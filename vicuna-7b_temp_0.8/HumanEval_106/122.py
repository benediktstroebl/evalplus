
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # print("Enter n :")
    n = int(input("Enter n : "))
    # Initialize the list with 1
    list_of_numbers = [1]
    # Iterate through the elements of the list
    for i in range(1, n + 1):
        # If i is even, add the factorial of i to the list
        if i % 2 == 0:
            list_of_numbers.append(i)
        # If i is odd, add the sum of numbers from 1 to i to the list
        else:
            list_of_numbers.append(sum(range(1, i + 1)))
    # Return the list
    return list_of_numbers
