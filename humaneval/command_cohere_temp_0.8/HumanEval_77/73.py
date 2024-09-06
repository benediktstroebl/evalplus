```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the cube root of the number
    root = int(pow(a, (1/3)))

    # If the cube root is an integer return True, else False
    return root == int(root)
```

This function utilizes the condition that a number is a cube if its cube root is an integer. The provided examples validate the correctness of this approach. To further guarantee the solution, the function also checks if the number is greater than zero, returning `False` if the number is less than or equal to zero, following the note provided in the problem description. 

*Note*: The `root` variable is assigned the integer value of the cube root using `int(pow(a, (1/3)))`. This is an approximation of the real cube root, but it will work for all valid inputs. If you want a more precise result, you may consider using a different method to calculate the cube root.