```python
def add(x: int, y: int):
    return x + y
```
The function takes in two arguments, x and y, both of type integer, and it returns the sum of the two values. 

To verify the functionality, you can test the function by calling it with two integers a and b and comparing the returned value with the expected sum 'a+b'. 

For example:
```python
# test the function
a = 2
b = 3
expected = a + b
actual = add(a, b)

print(f'Add two numbers {a} and {b}:')
if actual == expected:
    print('Passed')
else:
    print('Failed')
```
This would yield the following output:
```python
Add two numbers 2 and 3:
Passed
```

This demonstrates that the function correctly adds two numbers as expected.