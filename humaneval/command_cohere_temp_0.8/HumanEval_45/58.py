```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle. 
    """
    return 0.5 * a * h
```

To ensure the robustness of the function, test cases should be added to cover different scenarios, capturing edge cases and various inputs. The function's docstring includes information about the expected arguments and the return value, which is important for documentation purposes. Furthermore, to enhance its usability, the function could optionally handle incomplete inputs, such as when 'a' or 'h' is missing or None, thus enabling more flexible usage.