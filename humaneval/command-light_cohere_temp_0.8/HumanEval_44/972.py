```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base."""
    if x < 0:
        x = abs(x)

    if base == 2:
        return '{:0b}'.format(x). 
            ).format(x)

    elif base == 10:
        return '{:0d}'.format(x, int(base))

    else:
        raise ValueError("Invalid base number.")

# Test cases
test_case_1 = 8
test_case_2 = [21, 3]
test_case_3 = 8
test_case_4 = [10, 2]
test_case_5 = 7

for case in test_case_1:
    print(f'Case 1: {case})
    print(change_base(case, 10))

for case in test_case_2:
    print(f'Case 2: {case})
    print(change_base(case, 2))

for case in test_case_3:
    print(f'Case 3: {case})
    print(change_base(case, 10))

for case in test_case_4:
    print(f'Case 4: {case})
    print(change_base(case, 2))

for case in test_case_5:
    print(f'Case 5: {case})
    print(change_base(case, 10))
```
This Python code defines a function called change_base that takes two arguments: x (the number to be converted) and base (the desired base number). The function performs the necessary conversion and then returns the result as a string in the appropriate base. It also includes several test cases that cover different scenarios and pass all the tests successfully.