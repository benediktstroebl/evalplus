```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The given function checks two conditions:
1. Whether the type of `n` is int to ensure the base is an integer.
2. Whether `x` can be written as `n ** int(x)` to ensure if it's a simple power. 

The function returns `True` if both conditions are satisfied, otherwise, it returns `False`. 

The markdown code block for the solution is formatted below:
```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

Ensure the indentation is consistent with the code block in your original prompt. 

This way, the solution can be readily copied and run as a standalone Python script. 
If you'd like to test it, you can write some test cases in the same file or paste the function in another Python file and call it with different inputs. Fuzzing it with a wider range of inputs can also be useful to ensure its robustness. 
Feel free to adapt the solution further or ask if you need any further assistance!