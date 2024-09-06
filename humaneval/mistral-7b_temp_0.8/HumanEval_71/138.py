
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # A, B and C are the three sides of the triangle
    # Write your code here
    sum_of_two = 0
    triangle_area = 0

    if a + b > c and b + c > a and c + a > b:
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j:
                    sum_of_two = a[i] + b[j]
                    triangle_area = sum_of_two * c[i]

        return triangle_area
    else:
        return -1
