```python
def iscube(a):
    if a < 0:
        a = -a
    if a > 0:
        return a ** 3 == int(a ** 3)
    else:
        return a == -a ** 3
```
This function utilizes basic mathematical properties of cubes. It operates by first determining if the number is negative. If the number is negative, it then confirms whether the magnitude of the number is the cube of an integer. If the number is positive, it checks if the number is equal to the cube of an integer. This approach eliminates the need for complex calculations, making it efficient and straightforward.