```python
def specialFilter(nums):
    oddDigits = ['1', '3', '5', '7', '9']

    return sum(1 for num in nums if num > 10 and (num%10) in oddDigits and (num%100) in oddDigits)
```

The function `specialFilter` leverages list comprehension and conditional statements to calculate the sum of numbers that fulfill the problem statement's criteria. The tests for the function would depend on the intended input range and scenarios; providing specific tests would help ensure the function's robustness and accuracy. Feel free to add more tests according to your specific needs, and if you have more questions or need further assistance, please let me know!