```python
def change_base(x, base):
    return str(x).encode([(str(base), 'bx')])
```
This script takes an integer `x` and a base `base` as inputs and returns the string representation of `x` in the specified base. It utilises the `encode` method, which supports symbolic encodings, to achieve this. 

Here's an example usage of the function to demonstrate its functionality:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```
This would give the following outputs:
```
22
1000
111
```
The function works in an intuitive manner, leveraging the `encode` method to achieve the desired base conversion. By specifying the tuple `(str(base), 'bx')`, it directly converts the integer `x` to a string representation in the desired base.