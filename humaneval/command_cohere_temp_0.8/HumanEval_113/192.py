```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for digit in digits if digit % 2 == 1)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This solution uses a simple algorithm that iterates through each string `digits` in the list and calculates the count of odd digits in the loop, with alinecually appending the results to a list `r`. The final result is returning the list of strings with the necessary substitutions as mandated by the problem statement.

The problem is basically a twist on a classic algorithm design problem - counting odd characters (or in this case, odd digits) in a string, and this solution showcases an efficient approach to tackling such problems. It maintains readability while effectively solving the problem.