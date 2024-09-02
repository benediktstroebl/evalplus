
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
    
    def a_to_base_3(a):
        a_exp = 0
        while a != 0:
            a_exp += 1
            a = a / 3
        return a_exp
    
    def base_3_to_a(a):
        base_3_exp = 0
        while a_to_base_3(a) != base_3_exp:
            a = a * 3
            base_3_exp += 1
        return a
    
    return a_to_base_3(a) == base_3_to_a(a)