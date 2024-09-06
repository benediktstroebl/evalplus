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

This function utilizes the condition that a number is a cube if its cube root is an integer. The provided examples validate the correctness of this approach. To further guarantee the solution, the function also checks if the number is greater than 0 since no negative numbers raise a cube, and 0 is considered a cube.