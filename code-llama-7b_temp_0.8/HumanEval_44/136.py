

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    #convert number to string
    x = str(x)
    #initialize a list to store the digits of the output
    y = []
    #for each character in the string of the input number
    for i in range(len(x)):
        #append the number of that character times the power of the base
        #to the list
        y.append(x[i] * (base**(len(x)-(i+1))))

    #return the string representation of the number
    return str(sum(y))
