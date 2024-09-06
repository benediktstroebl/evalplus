```python
def number_of_odd(lst):
    r = []
    for x in lst:
        # remove all digits
        temp = str(x).replace('0','')
        # count odd numbers
        number_odd = len(temp) % 2
        # add to result
        r.append(f'the number of odd elements in the string {number_odd} of the input.')
    return r
```

The solution utilizes a basic python for loop to iterate through the list of strings. For each string, it removes all digits using `replace('0','')`, which leaves only odd or even spaces behind depending on whether the string had an odd or even number of digits originally. Then it calculates the number of odd spaces, which corresponds to the number of odd digits in the original string, and appends this number to the result list. Overall, the solution does not use any advanced python features and is reasonably concise.