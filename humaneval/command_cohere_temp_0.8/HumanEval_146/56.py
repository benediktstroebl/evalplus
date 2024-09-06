```python
def specialFilter(nums):
    odd_digits = [int(num) for num in nums if num > 10 and (num % 10 != 0 or num // 10 != 0)]
    return len(odd_digits)
```

This function `specialFilter` takes an array of numbers (`nums`) as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits.

The conditional statements within the function check if each number in the array (`num`) is greater than 10 and if both the first digit (using modulus `%`) and the last digit (using division `/`) of each number are odd. The `if` statement combines both conditions with the logical operator `and`.

Should you want to test this function, you can call it with a list of numbers, and it will return the count of numbers that fulfill the specified criteria.