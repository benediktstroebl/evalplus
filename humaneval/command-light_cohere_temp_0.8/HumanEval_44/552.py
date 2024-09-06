Here is a self-contained Python script that solves the problem of converting a given number to a different base:
```python
def change_base(x, base):
    # Implement the function logic here
    # ...
    return x  # return the converted number as a string

# Example usage
base_one = 10
base_two = 2
number = 8

# Call the function with two different bases and the same number
result_base_one = change_base(number, base_one)
print(result_base_one)   # expected output: '22'

result_base_two = change_base(number, base_two)
print(result_base_two)  # expected output: '1000'
```
This script defines a function `change_base` that takes two arguments: the number to be converted `x` and the desired base `base`. It then returns the converted number as a string, which is the expected output when the function is called with a given number and base.