Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    less_than_n = [int(x) for x in range(n - 1, 1, -1)]
    return sum(1 for x in less_than_n if x % 11 == 0 or x % 13 == 0 and 7 in str(x))
```
This function uses a list and a generator expression to efficiently filter the relevant numbers and count the occurrences of 7 in a one-liner. Tests are not included, but feel free to add your own to verify the functionality. 
Let me know if you'd like me to take a specific approach and I'll modify the script accordingly. Feel free to provide additional details or specifications and I'll make sure the solution caters to your needs.