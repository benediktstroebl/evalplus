```python
def fibfib(n):
    # Handle special cases (similar to Fibonacci)
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Use a recursive approach
    # Each recursive call eliminates the two last elements of the sequence
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Unit tests
print(fibfib(1))
print(fibfib(5))
print(fibfib(8))
```

You can copy and paste this code into a Python environment or script, and it will execute the function fibfib with the provided test cases. 

The approach is similar to the Fibonacci sequence: it uses a recursive approach, but instead of summing up two previous elements, it sums up the second last, third last, and so on, elements of the sequence. 

Please let me know if this solution suits your needs or if you would like me to provide an alternative approach. I can also explain how this solution works in case you are interested in the logic behind it!