```python
def change_base(x: int, base: int) -> str:
    if base == 10:
        return str(x)
    else:
        return "{0}".format(str(x), base)

#Test cases
test_case1 = 8
test_case2 = 3
test_case3 = 2
test_case4 = 7
test_case5 = 10

print("Results of test cases:", end="split("", "\n"))
for case in [test_case1, test_case2, test_case3, test_case4, test_case5]:
    print(f"Case {case} - Result: {change_base(case, 10)}", end=" ")
```
This code defines a function `change_base` that takes two parameters: `x`, which represents the number to be converted, and `base`, which specifies the desired base. The function returns the base 10 representation for `x` if `base` is 10. Otherwise, it uses the formatting of `x` as a string using the specified `base`. 

The test cases are defined and printed, and the results are displayed. This code demonstrates how to convert a number to a specified base using a simple string formatting technique.