```python
def change_base(x, base):
    return str(x).encode('utf-8')[::base].decode('utf-8')
```
This function leverages Python's `encode` and `decode` methods to directly convert the input number to the specified base. This approach is both concise and efficient, bypassing the need for manual conversion or intermediate representations. Note that this solution assumes 'utf-8' encoding, which is compatible with Python's string handling. 

This function defines the given problem statement in a concise and elegant manner, showcasing the simplicity of the solution with the Python language.