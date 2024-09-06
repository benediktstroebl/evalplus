
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    else:
        return [lst[0], lst[-1]]

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = add(list1)
print(list3) #printing the result
print(list3 == [2, 10]) #testing if the result is equal to the expected result
