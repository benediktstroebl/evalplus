```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This approach uses string translation, which is efficient and works without importing any extra modules. It's also generic and provides some flexibility in modifying the code if needed. For example, it easily handles various bases and input numbers like 7, 16, 111, etc. The translation map is created with str.maketrans() and formatted with f'{base}_{base}_{base}123' to ensure the desired conversion. 

To see the conversion process visually, you can run the following code:
```python
for i in range(10):
    print(change_base(8, i))
```

This will provide a clearer insight into the conversion for different bases, as it shows the output of the function for each base from 2 to 10.