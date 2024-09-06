```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, 1):
        n = sum(int(d) % 2 == 1 for d in s)
        r.append(f"the number of odd elements in the string {i} of the input."
            .replace(str(i), f"{n}")
        )
    return r
```

This script defines a function `odd_count` which takes a list of strings as input and returns a list where each element is replaced with the number of odd digits in the corresponding string. The replacement is performed using string formatting with the `replace` method. The enumerate function is used to iterate through the list and the strings are processed with a generator expression that sums the odd digits. Overall, the code uses a concise and elegant approach that adheres to Python best practices.