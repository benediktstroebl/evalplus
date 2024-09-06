

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Implementation for the problem statement
    # Modify the code in any way you want to explore other variations of the problem
    # For example, you can try implementing the problem using a loop instead of recursion.
    # You can also try implementing the problem using a stack instead of recursion
    # Make sure to test your implementation on sample inputs and expected outputs
    # to ensure that the code is correct and produces the desired result

    # Recursive implementation
    return 1 if n == 0 else 11*fizz_buzz(n//11) + 7*fizz_buzz((n//11)%11) 
    
