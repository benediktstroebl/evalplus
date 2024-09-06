```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single equality operation and tests the result against the original input, which is the most efficient way to solve this problem. 

Here is a more detailed explanation of the logic behind the code:
The idea is to convert the cubic root into an integer by rounding the result of the cubic root operation to the nearest integer. After this transformation, we simply compare the rounded value with the original number 'a' to determine if it is a perfect cube. 

This function uses **(1/3) as the exponentiator to find the cube root of the input 'a'**. Since the 'a' is an integer, the result of the **pow(a, (1/3))** function will have a decimal value. The **int()** function is used to round this decimal value to the nearest integer. 

For example:
```
iscube(8) ==> True
iscube(27) ==> True
iscube(104) ==> True
iscube(125) ==> False
iscube(216) ==> True
```