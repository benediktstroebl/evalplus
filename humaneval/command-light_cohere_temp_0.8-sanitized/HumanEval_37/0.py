def sort_even(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    odd.append(num)
   
    return even + odd