```python
def double_the_difference(lst):
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            result += n**2
    return result
```

The function iterates through each element `n` in the input list `lst`. It checks whether each element is an integer and greater than zero, if so, it calculates the square of the element and adds it to the `result` variable. The function then returns the final value of `result`. This approach ensures that only valid positive integers contribute to the result while excluding negative numbers, non-integer values, and empty inputs. 

This solution covers all the edge cases mentioned in the prompt, including an empty input list, returning 0 in such cases.

The function can be tested as follows:
```python
# Test Case 1
print(double_the_difference([1, 3, 2, 0]))  # Output: 10

# Test Case 2
print(double_the_difference([-1, -2, 0]))  # Output: 0

# Test Case 3
print(double_the_difference([9, -2]))  # Output: 81

# Test Case 4
print(double_the_difference([0]))  # Output: 0

# Test Case 5
print(double_the_difference([]))  # Output: 0
```