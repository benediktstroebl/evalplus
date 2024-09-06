
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # TODO
    # return the list
    # with all even numbers between a and b, in ascending order
    # raise TypeError if either of a or b are not integers

    if not(isinstance(a, int) and isinstance(b, int)):
        raise TypeError
    if a>b:
        a,b=b,a
    for x in range(a,b+1):
        if x%2==0:
            print(x)

    # 1. Add the code to check that the inputs are integers
    # 2. If not, raise a TypeError

    # 3. Add the code to check that a is less than b
    # 4. If not, swap them

    # 5. Add the code to print the values

    # 6. Return the list, even if it is empty

