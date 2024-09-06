```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for _ in range(len(digits)) if digits[_] % 2 == 1))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

The code leverages Python's `str.format()` to substitute the indices with the count of odd digits. The resulting string is then appended to the `r` list. Overall, the solution is concise and efficient, adhering to Python's minimalist philosophy, and maintaining readability with an implicit understanding of the problem statement.