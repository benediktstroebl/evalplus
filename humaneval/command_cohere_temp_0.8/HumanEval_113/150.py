```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, 1):
        n = sum(int(d) % 2 == 1 for d in s)
        r.append(f"the number of odd elements in the string {i} of the input."
                 .replace(f'{i}', f"{n}"))
    return r
```

The code uses a simple `foreach` loop to iterate through the list of strings `lst`. For each string, it calculates the count of odd digits and substitutes it into the template string, which remains constant in the code. The final result is a list of strings containing the desired output.