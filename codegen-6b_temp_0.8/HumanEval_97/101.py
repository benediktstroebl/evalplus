
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
    assert type(a) == int, 'a must be an integer'
    assert type(b) == int, 'b must be an integer'
    assert a >= 0, 'a must be positive'
    assert b >= 0, 'b must be positive'
    
    def get_unit_digit(n):
        """Return the unit digit of n in base 10.
        
        Examples:
        get_unit_digit(148) returns 4
        get_unit_digit(20) returns 1
        get_unit_digit(11) returns 1
        get_unit_digit(12) returns 0
        get_unit_digit(13) returns 1
        get_unit_digit(18) returns 4
        get_unit_digit(19) returns 0
        get_unit_digit(28) returns 3
        """
        assert type(n) == int, 'n must be an integer'
        assert n >= 0, 'n must be positive'
        if n == 0: return 0
        if n < 10: return n
        digit = (n % 10) * get_unit_digit(n//10)
        if digit > 9:
            return 1
        return digit
    
    return get_unit_digit(a) * get_unit_digit(b)

