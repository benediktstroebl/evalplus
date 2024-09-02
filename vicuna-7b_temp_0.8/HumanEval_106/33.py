
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # Initialize the list with 1 as the first element
    list_of_numbers = [1]
    # Iterate through the elements of the list
    for i in range(n):
        # Initialize a variable to store the value of the current element
        current_value = list_of_numbers[i]
        # If the current element is even, multiply it with the factorial of its current index
        if i % 2 == 0:
            current_value = current_value * (i // 2)
        # Otherwise, add the sum of the numbers from 1 to the current element
        else:
            current_value = sum([list_of_numbers[j] for j in range(i, n + 1)])
        # Append the current value to the list of numbers
        list_of_numbers.append(current_value)
    return list_of_numbers
