```python
def solution(lst):
    odd_even = []
    even_sum = 0
    for num in lst:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_even.to include num 
    return evensum + even_sum

# Example 1
solution([5, 8, 7, 1]) ==> 12

# Example 2
solution([3, 3, 3, 3, 3]) ==> 9

# Example 3
solution([30, 13, 24, 321]) ==> 0
```