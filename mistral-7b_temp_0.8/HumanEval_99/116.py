
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    #your code here
    closest_integer_list=[]
    for i in value:
        if i=='.':
            break
        else:
            closest_integer_list.append(i)
    closest_integer_list.append('.')
    for i in range(0,len(closest_integer_list)):
        if i==0 or i==len(closest_integer_list):
            pass
        else:
            if i==len(closest_integer_list)-1:
                x=closest_integer_list[i]+closest_integer_list[i-1]
                closest_integer_list[i]=x
                closest_integer_list[i-1]='0'
            else:
                x=closest_integer_list[i]+closest_integer_list[i-1]
                closest_integer_list[i]=x
                closest_integer_list[i-1]='0'
    for i in range(0,len(closest_integer_list)-1):
        if closest_integer_list
