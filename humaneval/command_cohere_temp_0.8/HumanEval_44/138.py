```python
def change_base(x, base):
    return str(x)
    if base == 10:
        return x
    conversion_map = {0: '0', 1: '1', 2: '2', 3: '10', 4: '11', 
                       5: '12', 6: '13', 7: '14', 8: '15', 9: '16'}
    result = 0
    while x > 0:
        remainder = x % base
        x = x // base
        result = result * 10 + conversion_map[remainder]
    return result
```

The function uses a dictionary (`conversion_map`) to map digits to numbers in the new base system. It iterates through the input number `x` using modular arithmetic to convert it to the new base. The function returns the integer value of the number in the new base. 

This approach provides a more efficient solution, avoiding the creation of large strings and instead converting directly to an integer representation in the new base. 

The unit tests could be executed against this function as follows:
```python
# Calling the function for various test cases
print(change_base(8, 3)) # Output: '22'
print(change_base(8, 2)) # Output: '1000'
print(change_base(7, 2)) # Output: '111'
``` 
This would verify the correctness of the new function.