
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    d = {
            'apples':0,
            'oranges':0,
            'mangoes':0,
            'mango':0,
            'orange':0,
            'grapes':0,
            'grape':0,
            'grapes_of_course':0,
            'grapefruit':0,
            'grapes_of_course_and_grape':0,
            'grapefruit_and_grapes':0,
            'grapes_and_oranges':0,
            'grapes_and_grapes_of_course':0,
            'grapes_and_grapes_of_course_and_grapefruit':0,
            'grapes_and_grapes_of_course_and_grapes':0,
            'grapes_and_grapes_of_course_and_grapes_of_course':0,
            'grapes_and_grapes_of_course_and_grapes_of_course_and_grape':0,
            'grapes_and_grapes_of_course_and_grapes_of_course_and_grapes_of_course':0,
            }
    for c in s:
        if c =='grapes' or c =='grapefruit' or c == 'grapes_of_course' or c =='grapes_of_course_and_grape' or c == 'grapes_and_grapes_of_course':
            d[c] += 1
        if c =='grapes_of_course_and_grapefruit' or c == 'grapes_and_grapes_of_course_and_grape':
            d[c] += 1
            d['mangoes'] += 1
        if c =='oranges' or c == 'grapes_and_oranges':
            d['oranges'] += 1
            d['apples'] += 1
        if c == 'apples' or c =='oranges' or c =='grapes' or c =='g