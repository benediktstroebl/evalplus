
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
    n = len(str(value))
    if n % 1 == 0:
        return int(value)
    if abs(value-int(value)) < abs(value-int(int(value)+1)) or abs(value-int(int(value)-1)) < abs(value-int(value)):
        return int(value)+1
    return int(value)

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))
\end{code}

Answer: Here's a solution that works for both positive and negative numbers:

\begin{code}
