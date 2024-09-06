```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Find the integer cube root of the number
    cube_root = int(pow(a, (1/3)))

    # Check if the original number is equal to the cube
    return a == cube_root ** 3
```

This function employs integer cube root computation by raising the number to the power of (1/3) and then checks if the cube root repeats the original number when raised to the power of 3. It also handles negative inputs by excluding them in the validation since cubes of negative numbers are negative as well. Lastly, it returns True for zero and handles various integer inputs as cubes.