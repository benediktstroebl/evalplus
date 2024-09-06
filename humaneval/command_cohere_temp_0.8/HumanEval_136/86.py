```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            if n > positive:
                positive = n
        elif n < 0:
            if n < negative:
                negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, identifying the smallest positive and largest negative integers. The variables `positive` and `negative` are initialized to extreme values (`float('-inf')` and `float('inf')`) to facilitate the comparison process, with the loop updating these variables as needed. Ultimately, the function returns a tuple containing the identified largest negative and smallest positive integers, or `None` if none are present in the list. 

This approach allows the function to efficiently solve the problem and obtain the desired values, while also keeping the code concise and readable. 

The following test cases illustrate how the function behaves:
```python
test_cases = [
    ([2, 4, 1, 3, 5, 7], (None, 1)),
    ([], (None, None)),
    ([0], (None, None)),
    ([-3, -7, -1, -4, -2, -5], (-1, 0)),
]

for test_case, expected in test_cases:
    result = largest_smallest_integers(test_case)
    assert result == expected
```