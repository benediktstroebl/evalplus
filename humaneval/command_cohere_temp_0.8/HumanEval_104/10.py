```python
def unique_digits(xs):
    odd_digits = [int(''.join(x for x in str(n) if x.isdigit() and x % 2 != 0)) for n in xs if n > 0]
    return sorted(odd_digits)
```

The function `unique_digits` works by first filtering out odd digits from the positive integers in the input list `xs`. It converts each positive integer into a string, loops through each digit, and checks if the digit is odd. It uses the conditional statement `x.isdigit() and x % 2 != 0` to check if the current digit is odd. After collecting all odd digits, it converts them back to integers and returns them as a list. Finally, the list is sorted in ascending order using the `sorted` function.

The test cases are not provided in the original problem statement. Therefore, you'll need to create test cases to validate the function. Here's an example:
```python
# Test case: [15, 33, 1422, 1]
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

# Test case: [152, 323, 1422, 10]
assert unique_digits([152, 323, 1422, 10]) == []

# Test case: [421, 134, 99, 59, 25]
assert unique_digits([421, 134, 99, 59, 25]) == [421, 134, 99, 59, 25]
``` 
You can modify and add more test cases as needed to cover different scenarios.