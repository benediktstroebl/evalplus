
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    #filter is a function in python 3 which removes the numbers
    #that are not greater than 10
    # .filter() first argument is a function that takes an array element and returns a Boolean
    # .filter() second argument is the array
    new_list = filter(lambda x:x > 10, nums)
    new_list2 = list(new_list)
    for i in new_list2:
        #check if first and last number are odd
        if not i%2 == 0:
            #check if first and last number are odd
            if i%10 != 0:
                print(i)



