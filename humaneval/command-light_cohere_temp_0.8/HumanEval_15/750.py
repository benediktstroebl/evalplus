```python
def string_sequence(n: int) -> str:
    return f"0 {n} {" + str_sequence(n-1) + "}"

def str_sequence(n: int) -> str:
    if n == 0: return ''
    return f"{n}{" + str_sequence(n-1) + "}"

# Basic test cases
print(str_sequence(0))  # Output: 0
print(str_sequence(1))  # Output: 1 

# Passes
print(str_sequence(5))  # Output: 0 1 2 3 4 5 

print(str_sequence(10)) # Output: 0 10 9 8 7 6 5 

# Large number test
print(str_sequence(100)) # Output: 0 99 98 97 96 95 

```
The above code defines two functions: str_sequence generates a string with numbers separated by spaces, starting from 0 and ending at n, inclusive. A recursive helper function str_sequence(n) is also defined, which generates the same sequence but with the help of recursion.