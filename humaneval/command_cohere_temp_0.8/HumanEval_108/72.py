```python
def count_nums(arr):
    num_sum = 0
    for n in arr:
        s = str(n)
        if s[0] != '-' and sum(int(d) for d in s) > 0:
            num_sum += 1
    return num_sum
```

This approach converts each input number n in the array to a string, and checks if the first character of this string is a hyphen '-'. If it is not a hyphen, the sum of the digits of the number is greater than 0. Thus, the function increments the count num_sum by 1 for each number with these properties. The resulting count is returned from the function.

This solution corresponds to the test cases outlined in the original problem, namely that the function:
- Returns 0 when the input array is empty [];
- Returns 1 when the array contains the items [-1, 11, -11] ;
- Returns 3 when the array contains the items [1, 1, 2]. 

The script can be tested against these use cases to verify its functionality.