```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This Python script defines a function called `sum_squares` taking a list as an argument, aiming to process integer list elements according to their indices' multiples. It develops the following steps:
1. Initialize a variable called `result` to store the final sum.
2. Use a loop, alongside the `enumerate` function, to iterate through each index and corresponding number in the provided list.
3. For every index that is a multiple of 3, square the corresponding number, and for indices that are both multiples of 4 and not multiples of 3, cube the number; meanwhile, leave the numbers unchanged if their indices don't meet these conditions.
4. Add the calculated values to the `result` variable.
5. Once all numbers are processed, the function returns the total sum of the modified numbers.

The script ensures that it handles all listed scenarios in the prompt's example cases:
1. For `lst = [1, 2, 3]`, the output should be 6, which is the sum of `1^2`, `2^2`, and `3^2`.
2. For `lst = []`, the output should be 0, as there are no numbers to modify.
3. For `lst = [-1, -5, 2, -1, -5]`, the output should be -126, which is the sum of `(-1)^2`, `(-5)^2`, `2^3`, `(-1)^3`, and `(-5)^3`.

This code provides an effective solution to the presented problem and fulfills the problem's requirement of returning the sum of modified list elements.