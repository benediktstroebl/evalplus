```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Find the smallest integer b whose cube is a
    for b in range(1, int(a**(1/3)) + 1):
        if a == b**3:
            return True

    return False
```

The function iterates through integers from 1 to the cube root of the number and checks if any of them is a cube of the number. As indicated in the prompt, this problem assumes that the input is always valid, and therefore does not check for edge cases such as 0 or infinities. The provided code block adheres to this assumption and does not account for these cases. 
If you would like to include this checks or any others that you consider relevant, it can be incorporated into the code like this: 
```python
def iscube(a):
    # Check if the number is positive
    if a <= 0:
        return False 
    elif a == 0:
        return True

    # Check if the number is an integer
    if a % 1:
        return False 
    elif a == 1:
        return True

    # Find the smallest integer b whose cube is a
    for b in range(1, int(a**(1/3)) + 1):
        if a == b**3:
            return True

    return False
``` 

Let's take a look at some of the lines of code and their purpose: 

1. **Positive Check**: This condition guarantees that the input is a positive number. If a is less than or equal to 0, it returns False, immediately ruling out any negative numbers, zero, or negative infinities. It's worth noting that this is the only place where a check for negativity is performed. 

2. **Integer Check**: The condition a % 1 checks if a is an integer. If a is not an integer (i.e., it has a fractional part), it returns False. This ensures that the result is only True for perfect cubes of positive integers. This is a stricter requirement compared to the original prompt, but it aligns with the principle of validating input. 

3. **Cube Root Search**: The loop iterates through potential cube candidates b, ranging from 1 to the cube root of a. It efficiently searches for the smallest integer b whose cube matches the input a. 

4. **Return True**: Once a matching cube is found, it returns True, indicating that the input is a cube of some integer. 

This updated version of the function incorporates the mentioned edge cases and provides a more robust and defensively programmed function.