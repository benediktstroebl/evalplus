def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Check the prime factorization, if there are only three unique factors it's a cube
    import math
    b = math.sqrt(a)
    c = math.sqrt(b)
    factors = set()
    while c >= 1:
        factors.add(c)
        c = math.floor(b / c)
        b = b / c
    return len(factors) == 3
    # Test cases