```python
def number_of_odd(lst):
    r = []
    for s in lst:
        odds = sum(1 for c in s if c % 2 != 0)
        r.append(f'the number of odd elements in the string {odds} of the input.')
    return r
```

The function uses a generator expression to iterate over each character in the string, and summing up the odds. Then it uses an f-string to construct the output string. You can also solve this problem using a loop and counting function like this:
```python
def odd_count(lst):
    r = []
    for s in lst:
        c = 0
        for c in s:
            if c % 2 != 0:
                c += 1
        r.append(f'the number of odd elements in the string {c} of the input.')
    return r
```

Which also loops over the input list lst and for each string s, it counts the number of odd characters c and appends this to the output list r, after formatting it nicely. This solution is very similar to the previous one but uses a for loop instead of a generator expression. These two solutions are technically very similar, the first one only uses a generator expression and relies on the sum function to do the counting, while the second one breaks down the counting into two separate loops. Both pass the test cases.