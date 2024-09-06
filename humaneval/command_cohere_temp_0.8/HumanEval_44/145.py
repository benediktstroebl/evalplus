```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}>{base}>{base}>{base}'))
```

This approach takes advantage of the built-in method `translate` found within a string. The `translate` method essentially replaces each digit with the specified translation string, which is formatted to the new base and hence returns the number in the desired base.

To test the function, one can create a string assertion with the desired output format or utilize the `translate` method directly on a string assertion to verify the output.

For instance, this would be a test that could be run to verify the function:
```python
assert change_base(8, 3) == '22'
```

Alternatively, you can use the method described above in the following manner:
```python
assert '8'.translate(str.maketrans('123456789', f'3>3>3>3')) == '22'
``` 

This approach allows us to test the function without adding unnecessary overhead within the tests themselves.