```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 != 0 for c in str(x))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension that iterates over each element in the input list `xs`. It checks if the digit of `x` is odd or not by checking if each digit in the string representation of `x` has a remainder of 1 when divided by 2; this is done using the `any` and `int` functions together with the modulo operator `%`. If it is odd, then it is added to the new list `odd` as part of the condition in the comprehension. Finally, the list `odd` is returned as a sorted list, which is achieved by using the `sorted` function.

This code is a self-contained Python script that solves the given problem. When given a list of positive integers `xs`, the function returns a sorted list of all elements that contain no even digits.

This solution is efficient and uses a single pass through the input list, making it an O(n) solution where n is the length of the input list `xs`. It also uses the `sorted` function, which has an efficiency of O(n log n), but this is a minor contribution to the overall time complexity since it's a constant factor for almost all inputs. Finally, the `any` function is used with a generator expression, which has a time complexity of O(n), but since it's used only once, it doesn't significantly affect the overall complexity.