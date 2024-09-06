
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    l = []
    for i in range(0,n//2):
        l.append(2*i)
    for i in range(0,n//3):
        l.append(4*i)
    for i in range(0,n//5):
        l.append(5*i)
    for i in range(0,n//7):
        l.append(7*i)
    for i in range(0,n//11):
        l.append(11*i)
    for i in range(0,n//13):
        l.append(13*i)
    for i in range(0,n//17):
        l.append(17*i)
    for i in range(0,n//19):
        l.append(19*i)
    for i in range(0,n//23):
        l.append(23*i)
    for i in range(0,n//29):
        l.append(29*i)
    for i in range(0,n//31):
        l.append(31*i)
    for i in range(0,n//37):
        l.append(37*i)
    for i in range(0,n//41):
        l.append(41*i)
    for i in range(0,n//43):
        l.append(43*i)
    for i in range(0,n//47):
        l.append(47*i)
    for i in range(0,n//53):
        l.append(53*i)
    for i in range(0,n//59):
        l.append(59*i)
    for i in range(0,n//61):
        l.append(61*i)
    for i in range(0,n//67):
        l.append(67*i)
    for i in range(0,n//71):
        l.append(71*i)
    for i in range(0,n//73):
       
