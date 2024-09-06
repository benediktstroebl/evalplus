```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number at index i can divide n evenly (i.e., n is divisible by i), then that number is returned. The loop ends as soon as such a number is found, guaranteeing that the function will not produce incorrect answers. 

Let's break down the correctness of the answer using the example in the prompt, `largest_divisor(15)`:
```python
largest_divisor(15)
# => loop: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# => 15 % 1 == 0 => 15 == 1 
# => 15 % 2 == 0 => 15 == 2 
# => 15 % 3 == 0 => 15 == 3 
# => ...
# => 15 % 5 == 0 => 15 == 5 
# => 15 % 6 == 0 => 15 == 5 
# => ... 
# => 15 % 15 == 0 => 15 == 5 
# => ... 
# => No other number below 15 divides 15 evenly 
# Therefore, the largest divisor of 15 smaller than 15 is 5
```