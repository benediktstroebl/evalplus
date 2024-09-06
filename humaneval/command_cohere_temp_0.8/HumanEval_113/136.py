```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for _ in range(len(digits)) if digits[_] % 2 == 1))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

The solution utilizes a sum function employed within a str context, which helps to convert the result to a string. Subsequently, a list comprehension is employed to determine the count of odd elements within each string. Ultimately, the variable r stores the output, where each element represents the number of odd elements in the corresponding string within the input list.