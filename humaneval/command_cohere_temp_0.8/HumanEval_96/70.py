```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    numbers = []
    for num in range(2, n):
        if is_prime(num) and num < n:
            numbers.append(num)
            count += 1
            if count == n:
                break
    return numbers
```
The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number if it's prime using the `is_prime()` function, if the number is prime and less than `n`, it adds it to the `numbers` list and increases the `count` counter. When the counter equals `n`, it stops iterating and returns the list of prime numbers. 

You can test this function by calling it with different inputs to check if it's producing the expected output. 
For example:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(0)) # []
print(count_up_to(1)) # []
print(count_up_to(18)) # [2, 3, 5, 7, 11, 13, 17]
``` 
This should output the expected result for each case. 
If you have more questions or need further assistance with this problem or any other topic, let me know!