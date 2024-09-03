```python
def specialFilter(nums):
    odd_count = 0
    odd_first_digit = 0
    odd_last_digit = 0

    for num in nums:
        if int(num[0]) > 10 or int(num[-1]) > 10:
            odd_count += 1
        if int(num[0]) % 2 == 1 and int(num[-1]) % 2 == 1:
            odd_first_digit += 1
        if int(num[-1]) % 2 == 1 and int(num[0]) % 2 == 1:
            odd_last_digit += 1

    return odd_count, odd_first_digit, odd_last_digit
```
The code defines a function `specialFilter` that takes an array of numbers (`nums`) as input and returns three values: the count of numbers that are greater than 10 and both have odd first and last digits, as well as the number of elements that satisfy this condition in the array.