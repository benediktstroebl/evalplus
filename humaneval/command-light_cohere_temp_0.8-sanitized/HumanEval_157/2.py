def right_angle_triangle(a, b, c):
    return (a + b > c and b + c > a and c + a > b) and (a == b or c == a)