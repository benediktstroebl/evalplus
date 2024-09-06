```python
def odd_count(strings):
    r = []
    for string in strings:
        odds = sum(1 for c in string if c % 2 == 1)
        r.append(f"the number of odd elements in the string {odds} of the input")
    return r
```

This script defines a function `odd_count` which takes in a list of strings and returns a list where each element is a string containing the count of odd digits in the corresponding string from the input. The function uses a generator expression within the loop to calculate the odd digit count for each string, and then constructs the output string using the count.