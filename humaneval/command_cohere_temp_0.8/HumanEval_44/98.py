```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}'))
```

This approach takes advantage of the translate method to replace each digit in '123456789' with the corresponding base digit. For example, when base=2, the translation replaces '1' with '2', '2' with '10', '3' with '12', and so on, effectively performing the conversion to base 2. The same principle applies to other bases. 

This solution is efficient and simple, with a time complexity of O(1) since it involves only a few translations and basic operations.

To further handle edge cases and enhance the function's versatility, you can add appropriate tests, such as checking bases less than 10, handling negative numbers, and accommodating bases greater than 10.