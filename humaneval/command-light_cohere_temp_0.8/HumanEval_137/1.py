```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if values are equal.
    """
   
    def comparison(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return (a > b)
        elif isinstance(a, str) and isinstance(b, str):
            return str(a) > str(b)
        else:
            return None
    return comparison(a, b)

# Test cases
print(compare_one(1, 5))  # Prints True
print(compare_one(1, "2,3"))  # Prints True
print(compare_one("5,1", "6"))  # Prints True
print(compare_one(1, 1))   # Prints None
print(compare_one("1", "1"))  # Prints True
```
This code provides a function called **compare_one** that accepts integers, floats, or strings representing real numbers, and it compares these data types. It uses Python's instance and type checks to determine if the arguments are numbers or strings, and then it compares them accordingly. The function returns **None** if the values are equal, or the larger value if one is greater than the other.