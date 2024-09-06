```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs Python's array filtering methodology alongside the len() function to tally up the number of elements in the array that fit the stipulated criteria. The binary intersection operation (&) is utilized to slender down the array of integers to those that are both odd in the beginning and in the end. 

To ascertain the solution's efficacy, you can integrate it into a testing framework containing the following test cases:
```python
# Testing the function with a variety of inputs
print(specialFilter([15, -73, 14, -15]))  # 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # 2
print(specialFilter([11, 19, 27, -11, 100, -27, 51]))  # 3
print(specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))  # 10
```

This testing framework validates the function's behavior against a range of inputs, ensuring its correctness and capability to handle diverse scenarios.