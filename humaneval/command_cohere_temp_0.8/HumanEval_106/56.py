```python
def f(n):
    facts = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i if i % 2 == 0 else facts[i - 1] + i
    return facts
```
This Python script defines a function 'f' that takes an integer 'n' as input and returns a list where each element corresponds to the value stated in the problem statement. It utilizes a list 'facts' to store these computed values, where each iteration of a loop updates the appropriate index of this list based on the given logic.