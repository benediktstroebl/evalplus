Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp_num = abs(num)

    while temp_num != 0:
        digit = temp_num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        temp_num = temp_num // 10
    
    return (count_even, count_odd)

# Driver code
if __name__ == "__main__":
    print(even_odd_count(-12))  # (1, 1)
    print(even_odd_count(123))  # (1, 2)
```
This script will print the counts of even and odd digits in the given numbers -12 and 123, respectively. The output will be:
```
(1, 1)
(1, 2)
```
The function operates by first setting the variable count_even to 0 and count_odd to 0. It then iterates through the digits of the passed number in reverse order, counting the number of even and odd digits and storing them in the variables count_even and count_odd respectively. Finally, it returns the tuple of counts (count_even, count_odd).