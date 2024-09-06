
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    #This is an example of a brute force approach
    #You could also use a more efficient method like
    #checking if the integer is divisible by any of the cubes of 
    #1, 2, and 3
    #or using a set of precomputed values to check if the number
    #is a cube of any integer in that set
    
    #This is an example of a more efficient approach
    #using modulo operator and a set
    #a % 100 == 0 --> True
    #a % 10 == 0 --> True
    #You can check if a is a cube of some number by
    #checking if a % 100 == 0 and a % 10 == 0
    #And you can check if it is a cube of a number 
    #by checking if it is a cube of all the numbers in 
    #the set of integers from 1 to 1000
    #Then you can check if the number is a cube of a
    #number from 1 to 1000
    #if the number is in the set of cubes of the numbers
    #from 1 to 1000
    #then it is a cube of some integer
    return a % 100 == 0 and a % 10 == 0