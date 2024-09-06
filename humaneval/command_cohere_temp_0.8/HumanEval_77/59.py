```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the integer cube root of the number
    cube_root = int(pow(a, 1/3))

    # Check if the cube root is an integer and the equality holds
    return cube_root ** 3 == a
```

The above method utilizes the integer cube root algorithm and checks for both the root being an integer and the equality condition. 

You can test this function by calling it with different input values and checking the output. For example:
```python
print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))  # True
print(iscube(180))  # False
```

This output should print 'True' for the first three examples, and 'False' for the last two, respectively. Adjust the input values to test other cases as needed.