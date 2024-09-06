def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # All odd perfect cubes have a remainder of 0 when divided by 3
    return (a >= 0 and a ** (1/3) == int(a ** (1/3)) and not a % 3) or a == -1