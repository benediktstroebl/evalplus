
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    #Write your code here!
    result=[]
    while x>0:
        result.append(x%10)
        x=x//10
    result.append(result[0])
    if shift>len(result):
        return "".join(result[-shift:]+result[:-shift])
    elif shift<len(result):
        return "".join(result[-shift:])
    else:
        return "".join(result)
