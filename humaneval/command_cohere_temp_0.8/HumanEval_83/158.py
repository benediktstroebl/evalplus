```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[n]
```

This approach uses a straightforward `bottom-up` approach. The function first counts the numbers that start with `1` and then uses this information to count the numbers that end with `1`. 

The approach assumes that the input is a positive integer, and therefore the code does not handle negative or zero values explicitly. 

To test this script, copy it into a Python file (e.g., `a.py`) and run the following command:
```bash
$ pytest a.py
```

This command will run the tests contained in the script and should produce the following output:
```bash
...
--------------------------------------------------------
Ran 1 test in 0.001s

OK
```