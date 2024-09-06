```python
def odd_count(strings):
    r = []
    for string in strings:
        count = str(len(string) - len(set(string) & {x for x in string if x % 2 == 0}))
        r.append(f"the number of odd elements in the string {count} of the input.")
    return r
```

This script defines a function `odd_count` which takes in a list of strings and returns a list where each element is a string containing the count of odd digits in the corresponding string from the input. The function uses string manipulation to calculate the count of odd digits in each string and appends this to the list. The result is a list of strings providing the counts of odd digits in the input strings.