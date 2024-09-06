```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        try:
            return round((1.0 / 2) * (a * b * s[0] - a * c * s[1] + b * c * s[2]), 2)
        except ZeroDivisionError:
            return -1
    else:
        return -1
``` 

The problem is solved using the Heron's formula to calculate the area of the triangle which is `A = (1/2) * [ abc / s(s-a)(s-b)(s-c) ] `, where s is the semi-perimeter of the triangle. The three sides form a valid triangle according to the problem statement when the sum of any two sides is greater than the third side.