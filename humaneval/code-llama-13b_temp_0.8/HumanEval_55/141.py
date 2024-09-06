

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    def iterative(n):
        # Check if n is less than or equal to 1.
        # If it is, we have found our base case.
        if n <= 1:
            return n

        # Define our 2 variables, num1 and num2, that will represent
        # the last 2 numbers in our sequence.
        num1 = 0
        num2 = 1

        # We will set i to 2 because the num1 and num2
        # represent the 0th and 1st numbers in our sequence,
        # but we already know the answer to the 0th term.
        i = 2

        # We will loop through the sequence until we reach the nth term
        while i < n:
            # Set the value of our num1 variable equal to the sum
            # of the previous 2 numbers in our sequence
            num1 = num2 + num1
            # Shift everything over 1 spot
            num2 = num1 + num2
            # Increase i by 1
            i += 1

        # Return the answer
        return num2

    def recursive(n):
        # Check if n is less than or equal to 1.
        # If it is, we have found our base case.
        if n <= 1:
            return n
        # Otherwise, call the function again with n - 1.
        else:
            return recursive(n - 1) + recursive(n - 2)

    return recursive(n)

