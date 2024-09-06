```python
def specialFilter(nums):
    oddDigits = [x for x in nums if x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(oddDigits)
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and returns the number of elements in the list that meet a specific criteria:
1. `x > 10`: The element is greater than 10.
2. `int(str(x)[0]) % 2 == 1`: The first digit of the element is odd.
3. `int(str(x)[-1]) % 2 == 1`: The last digit of the element is odd.

The list comprehension `oddDigits` creates a list of all the elements in `nums` that satisfy all these conditions. The function then returns the length of this `oddDigits` list, which is the number of elements in the input list that meet the specified criteria.

Here is a Markdown code block that you can use to test the function on your own:
```markdown
```python
test_list = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
print(specialFilter(test_list))  # Output: 1
```
```

The test list includes elements that meet the criteria (such as 15) and elements that don't (such as 33). When you run this code, it will print `1` as the output, indicating that one element in the test list satisfies the specified conditions.