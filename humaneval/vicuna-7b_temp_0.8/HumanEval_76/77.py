
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Write the function
    def is_simple_power(x, n):
        # Check that n is positive
        if n < 0:
            return False

        # Check that n is not a power of another number
        for y in range(1, n + 1):
            if n % y == 0:
                return False

        # Check that n**int = x
        for i in range(1, int(n ** 0.5) + 1):
            if n ** i != x:
                return False

        return True

    # Test the function
    assert is_simple_power(1, 4) == True, is_simple_power(1, 4)
    assert is_simple_power(2, 2) == True, is_simple_power(2, 2)
    assert is_simple_power(8, 2) == True, is_simple_power(8, 2)
    assert is_simple_power(3, 2) == False, is_simple_power(3, 2)
    assert is_simple_power(3, 1) == False, is_simple_power(3, 1)
    assert is_simple_power(5, 3) == False, is_simple_power(5, 3)
