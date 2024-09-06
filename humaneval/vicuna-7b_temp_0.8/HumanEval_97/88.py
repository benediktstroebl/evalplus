
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Implement the function using recursion.
    # The base case is when the input is 0.
    # The recurrence is:
    #     10^n \* (d1 \* d2 \* ... \* d(n)) = 10^n \* d1 \* d2 \* ... \* d(n-1)
    #     10^(n-1) \* (d1 \* d2 \* ... \* d(n-1)) = 10^n \* d1 \* d2 \* ... \* d(n-2)
    #      ...
    #     10 \* d1 = d1
    # So the result of 10^n \* d1 is d1 and the result of 10^n \* d2 is d2
    return a*b
