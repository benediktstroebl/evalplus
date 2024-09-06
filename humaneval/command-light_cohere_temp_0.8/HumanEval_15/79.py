Here is a self-contained Python script with a function that solves the problem of creating a string of space-separated numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f"0 {n} {" + str_sequence(n - 1) + "}"

def str_sequence(n: int) -> str:
    for i in range(n):
        yield i, ' ' + str(i) 

# Test the above function
test_str_sequence = str_sequence(10)
print(test_str_sequence)
```
This function uses a generator expression to produce a string of space-separated numbers, and the function string_sequence uses this generator expression to generate the string for a given input n.