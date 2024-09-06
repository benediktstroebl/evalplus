```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        n = sum(int(d) % 2 == 1 for d in s)
        r.append(f"the number of odd elements in the string {i} of the input." if n == 1 else f"{n}n the string {i} of the input." )
    return r
```

The solution leverages Python's `enumerate` to iterate through the list of strings and generate the corresponding result string in a single pass. It uses `sum` along with a generator expression to calculate the count of odd digits in each string efficiently. The resulting strings are then appended to the result list. 

This approach eliminates the need for explicit loops and reduces the complexity of the code, making it more readable and maintainable. Let me know if you would like to know more about the problem-solving approach or any other topic you may be interested in!