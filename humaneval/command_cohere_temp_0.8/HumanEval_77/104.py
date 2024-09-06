```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some integer
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `pow(a, 1/3)` is equal to the rounded value of itself. It will return True if the number is a cube of some integer, and False otherwise. 

This approach has a time complexity of O(1) since it only requires one `pow` operation and one `round` operation to determine if the number is a perfect cube. 

This approach assumes that the input will always be a valid integer, which is the assumption stated in the prompt.