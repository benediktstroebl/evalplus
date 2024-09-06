```python
def skjkasdkd(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` uses a list comprehension to filter out prime numbers from the given list and then finds the largest prime number in that list. Finally, it returns the sum of the digits of the largest prime.

To test this, you can create a list of integers and pass it to the function to verify if it returns the correct output:
```python
# Test 1
lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
print(skjkasdkd(lst))  # Expected output: 10

# Test 2
lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]
print(skjkasdkd(lst))  # Expected output: 25

# Test 3
lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]
print(skjkasdkd(lst))  # Expected output: 13

# Test 4
lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6]
print(skjkasdkd(lst))  # Expected output: 11

# Test 5
lst = [0,81,12,3,1,21]
print(skjkasdkd(lst))  # Expected output: 3

# Test 6
lst = [0,8,1,2,1,7]
print(skjkasdkd(lst))  # Expected output: 7
``` 

This way, you can ensure that the function works as expected and provides the correct output for different test cases. 
Please note that the omitted tests will be skipped.  If you want to complete the testing process for the skjkasdkd function, let me know so I can provide more test cases.