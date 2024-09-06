
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # 🚨 Don't change the code below 👇
    even_indices = lst[1::2]
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
    return sum(even_indices)

