```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test the function with a variety of inputs
for n in range(0, 10):
    for input_str in ["[-10, 4, 6]", "[1, 2, 4, 5]", "[10, 20, 30]", "[4, 40, 60, 100]"]:
        result = median(input_str. Test the result using assert result == eval(input("Result: ") + str(n) + " = " + input_str)),
```