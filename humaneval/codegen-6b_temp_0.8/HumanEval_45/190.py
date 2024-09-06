

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h)/2


for line in fileinput.input("triangle.txt"):
    print(triangle_area(*[int(x) for x in line.split()]))
