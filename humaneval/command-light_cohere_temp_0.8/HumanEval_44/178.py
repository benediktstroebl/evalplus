```python
def change_base(x: int, base: int):
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Calculate the base value using n(base) times x.")
    return str(int(pow(base, x)))

x = 8
base = 2
try:
    print(change_base(x, base))
except ValueError as e:
    print(f"Error: {e}")
```
This code provides a function change_base that takes an integer x and an integer base as input. It then performs the value of the given formula and converts it into a string representation of the number using the specified base. The code also includes a try-except block that catches any ValueError that might occur if an invalid base value is provided. It then prints the specified error message.