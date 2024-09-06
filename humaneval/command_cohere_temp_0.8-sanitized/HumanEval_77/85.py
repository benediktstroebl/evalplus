def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Returing boolueana availible since Python 3.5, propose user to upgrate
    return a ** 3 == int(a ** 3)