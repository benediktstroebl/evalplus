```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single comparison, which speeds up the process.

Here is a more detailed explanation of the steps:
1. `a ** (1/3)`: This is the cube root of `a`. This step represents the power of a which would return the original number. 
2. `int(a ** (1/3))`: This returns the whole number value of the cube root. For example, the cube root of 81 is 9, but 81 is also a cube because it equals 3 x 3 x 3. 

Therefore, this function answers the question of whether a is a cube simply by comparing the two numbers returned above. 

This is a concise way to write the `iscube` function, but it does assume that the input is valid, as per the note in the prompt.