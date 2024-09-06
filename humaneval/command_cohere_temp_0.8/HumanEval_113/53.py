```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for _ in range(len(digits)) if digits[_] % 2 == 1))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

The code uses a generator expression along with the `sum` function to calculate the number of odd digits in a given string. The result is then formatted into a sentence that addresses the prompt's requirement and appended to the `r` list. Overall, the function takes a list of lists of digits as input and returns a list of strings with the desired message.