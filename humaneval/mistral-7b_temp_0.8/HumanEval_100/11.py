
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # Your code here
    n=int(input("Enter a number: "))
    print(n)
    l=[]
    if n%2==0:
        l.append(n)
        for i in range(2,n+1,2):
            l.append(i)
    else:
        l.append(n)
        for i in range(2,n+1,2):
            l.append(i+1)
    return l
    # In the following code, we have used the word 'n' in the function
    # make_a_pile(n) which is the same as the variable 'n' we defined in the
    # global scope. This is because of the concept of variable shadowing.
    # When we use 'n' in the function, we are creating a new variable 'n' that
    # shadows the 'n' defined in the global scope. This means that the 'n'
    # inside the function will be the one defined in the function and the 'n'
    # outside the function will be the one defined in the global scope.
    #
